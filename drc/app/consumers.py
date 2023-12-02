from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected....", event)
        print("CHANNEL LAYER👽: ", self.channel_layer)
        print("CHANNEL NAME💫: ", self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'djangosorous', 
            self.channel_name
            )
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self, event):
        print("Message Received....", event)
        async_to_sync(self.channel_layer.group_send)('djangosorous', {
            'type' : 'chat.message',
            'message' : event['text']
        })
        
    def chat_message(self, event):
        print("EVENT: ", event)
        print("Actual data: ", event['message'])
        self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    def websocket_disconnect(self, event):
        print("Websocket Disconnected....", event)
        print("CHANNEL LAYER👽: ", self.channel_layer)
        print("CHANNEL NAME💫: ", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'djangosorous', 
            self.channel_name
            )
        raise StopConsumer()
        
        
        
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected....", event)
        print("CHANNEL LAYER👽: ", self.channel_layer)
        print("CHANNEL NAME💫: ", self.channel_name)
        await self.channel_layer.group_add(
            'djangosorous', 
            self.channel_name
            )
        await self.send({
            'type':'websocket.accept'
        })
        
    async def websocket_receive(self, event):
        print("Message Received....", event)
        await self.channel_layer.group_send('djangosorous', {
            'type' : 'chat.message',
            'message' : event['text']
        })
        
    async def chat_message(self, event):
        print("EVENT: ", event)
        print("Actual data: ", event['message'])
        await self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected....", event)
        print("CHANNEL LAYER👽: ", self.channel_layer)
        print("CHANNEL NAME💫: ", self.channel_name)
        await self.channel_layer.group_discard(
            'djangosorous', 
            self.channel_name
            )
        raise StopConsumer()
        
       