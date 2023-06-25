from django.urls import re_path

from .consumers import TradeConsumer

websocket_urlpatterns = [
    re_path(r'ws/trade/$', TradeConsumer.as_asgi()),
]