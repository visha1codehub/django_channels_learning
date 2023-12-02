from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
import json
from .models import Chat, Group

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.group_namva = self.scope['url_route']['kwargs']['grpname']
        # user = self.scope['user']
        # print(user)
        print(f"Hii {self.group_namva}😀")
        async_to_sync(self.channel_layer.group_add)(
            self.group_namva, 
            self.channel_name
            )
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self, event):
        group = Group.objects.get(name=self.group_namva)
        user = self.scope['user']
        # print(user)
        content = json.loads(event['text'])['msg']
        if user.is_authenticated:
            chat = Chat(content=content, user=user, group=group)   #with user
            chat.save()
        else:
            chat = Chat(content=content, group=group)   #without user
            chat.save()
        data = json.loads(event['text'])
        data['user'] = user.username if user.is_authenticated else "anonymous"
        async_to_sync(self.channel_layer.group_send)(self.group_namva, {
            'type' : 'chat.message',
            'messageo' : json.dumps(data)
        })
        
    def chat_message(self, event):
        # print(event)
        self.send({
            'type' : 'websocket.send',
            'text' : event['messageo']
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
        group = database_sync_to_async(Group.objects.get)(name=self.group_namva)
        content = json.loads(event['text'])['msg']
        chat = Chat(content=content, group=group)
        await database_sync_to_async(chat.save())()     #?db sync to async
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
        
       