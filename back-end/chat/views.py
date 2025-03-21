# backend/chat/views.py

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Conversation, Message
from .serializers import (
    ConversationSerializer, 
    ConversationListSerializer, 
    MessageSerializer,
    MessageCreateSerializer
)
from .ai_service import get_ai_service
from accounts.models import UserProfile

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    
    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ConversationListSerializer
        return ConversationSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def rename(self, request, pk=None):
        conversation = self.get_object()
        title = request.data.get('title')
        if not title:
            return Response({'error': 'Título não pode ser vazio'}, status=status.HTTP_400_BAD_REQUEST)
        
        conversation.title = title
        conversation.save()
        return Response({'status': 'Conversa renomeada'})

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_pk')
        return Message.objects.filter(
            conversation_id=conversation_id,
            conversation__user=self.request.user
        )

class ChatBotView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        message_content = serializer.validated_data['content']
        conversation_id = serializer.validated_data.get('conversation_id')
        
        # Obter ou criar conversa
        if conversation_id:
            conversation = get_object_or_404(
                Conversation, 
                id=conversation_id, 
                user=request.user
            )
        else:
            # Criar nova conversa
            title = message_content[:30] + '...' if len(message_content) > 30 else message_content
            conversation = Conversation.objects.create(
                user=request.user,
                title=title
            )
        
        # Salvar mensagem do usuário
        user_message = Message.objects.create(
            conversation=conversation,
            role='user',
            content=message_content
        )
        
        # Obter todas as mensagens da conversa para contexto
        conversation_messages = list(Message.objects.filter(conversation=conversation))
        
        # Obter informações do perfil do usuário para personalização
        try:
            profile = UserProfile.objects.get(user=request.user)
            nivel_educacao = profile.nivel_educacao
            area_interesse = profile.area_interesse
        except UserProfile.DoesNotExist:
            nivel_educacao = None
            area_interesse = None
        
        # Gerar resposta com o serviço de IA
        ai_service = get_ai_service()
        ai_response = ai_service.generate_response(
            conversation_messages, 
            nivel_educacao=nivel_educacao, 
            area_interesse=area_interesse
        )
        
        # Salvar resposta da IA
        assistant_message = Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=ai_response
        )
        
        # Atualizar título da conversa se for nova
        if len(conversation_messages) <= 1:
            conversation.title = message_content[:30] + '...' if len(message_content) > 30 else message_content
            conversation.save()
        
        return Response({
            'conversation_id': conversation.id,
            'user_message': MessageSerializer(user_message).data,
            'assistant_message': MessageSerializer(assistant_message).data
        })