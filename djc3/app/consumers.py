from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected....", event)
        self.send({
            'type':'websocket.accept'
        })
        
    # def websocket_receive(self, event):
    #     # print("Message Received....", event)
    #     print("Message from client is : ", event['text'])
    #     for i in range(10):
    #         self.send({
    #         'type': 'websocket.send',
    #         'text': f"{i} Message from Sync server...."
    #         })
    #         sleep(1)
    
    def websocket_receive(self, event):
        # print("Message Received....", event)
        print("Message from client is : ", event['text'])
        for i in range(10):
            self.send({
            'type': 'websocket.send',
            'text': json.dumps({'count':i})   #sending python dictionary after changing it to string 
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print("Websocket Disconnected....", event)
        raise StopConsumer()
        
        
        
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected....", event)
        await self.send({
            'type':'websocket.accept'
        })
        
    async def websocket_receive(self, event):
        # print("Message Received....", event)
        print("Message from client is : ", event['text'])
        for i in range(10):
            await self.send({
            'type': 'websocket.send',
            'text': f"{i} Message from Async server...."
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected....", event)
        raise StopConsumer()