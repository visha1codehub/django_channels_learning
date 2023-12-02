from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected 😄....", event)
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self, event):   #!🤕 waste a lot of time for finding a jhaatu error that was 'recieve->receive'
        print("Message Received 🥰....", event)
        print("Message is : ", event['text'])
        self.send({
            'type': 'websocket.send',
            'text': "Message from server 😎...."
        })

    def websocket_disconnect(self, event):
        print("Websocket Disconnected 🥲....", event)
        raise StopConsumer()
        
        
        
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected 😄....", event)
        await self.send({
            'type':'websocket.accept'
        })
        
    async def websocket_receive(self, event):
        print("Message Received 🥰....", event)
        await self.send({
            'type': 'websocket.send',
            'text': "Message from server 😎...."
        })

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected 🥲....", event)
        raise StopConsumer()