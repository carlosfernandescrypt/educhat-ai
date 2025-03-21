# backend/chat/serializers.py

from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'role', 'content', 'created_at')
        read_only_fields = ('id', 'created_at')

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'created_at', 'updated_at', 'messages')
        read_only_fields = ('id', 'created_at', 'updated_at')

class ConversationListSerializer(serializers.ModelSerializer):
    message_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'created_at', 'updated_at', 'message_count')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def get_message_count(self, obj):
        return obj.messages.count()

class MessageCreateSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    conversation_id = serializers.IntegerField(required=False)