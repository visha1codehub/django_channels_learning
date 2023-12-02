from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:grpname>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:grpname>/', consumers.MyAsyncConsumer.as_asgi()),
]

 