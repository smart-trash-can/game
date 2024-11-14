import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from game import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tic_tac_toe.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/game/<str:room_name>/", consumers.GameConsumer.as_asgi()),
        ])
    ),
})
