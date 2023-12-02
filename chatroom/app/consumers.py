from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.group_namva = self.scope['url_route']['kwargs']['grpname']   #$ 'scope in consumers' is just like 'request in views'
        async_to_sync(self.channel_layer.group_add)(
            self.group_namva, 
            self.channel_name
            )
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self, event):
        async_to_sync(self.channel_layer.group_send)(self.group_namva, {
            'type' : 'chat.message',
            'message' : event['text']
        })
        
    def chat_message(self, event):
        self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_namva, 
            self.channel_name
            )
        raise StopConsumer()
        
        
        
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.group_namva = self.scope['url_route']['kwargs']['grpname']
        await self.channel_layer.group_add(
            self.group_namva, 
            self.channel_name
            )
        await self.send({
            'type':'websocket.accept'
        })
        
    async def websocket_receive(self, event):
        await self.channel_layer.group_send(self.group_namva, {
            'type' : 'chat.message',
            'message' : event['text']
        })
        
    async def chat_message(self, event):
        await self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.group_namva, 
            self.channel_name
            )
        raise StopConsumer()
        
       