from django.urls import path
from .consumers import ChatConsumer
from chatbot.consumers import ChatConsumer


websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),  # WebSocket route for chat
]
