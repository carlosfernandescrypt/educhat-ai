# backend/chat/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet, ChatBotView

# Configuração do router principal
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Router aninhado para mensagens
conversations_router = routers.NestedSimpleRouter(router, r'conversations', lookup='conversation')
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# URLs adicionais para chatbot
urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversations_router.urls)),
    path('message/', ChatBotView.as_view({'post': 'create'}), name='chatbot-message'),
]