from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, JsonWebsocketConsumer
import json

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("connected!")
        self.accept()
        # self.close(code=4123)    # to forcefully reject the websocket
        
    def receive(self, text_data=None, bytes_data=None):
        print("recieved from client", text_data)
        data = json.loads(text_data)
        self.send(text_data=f"from server to client.. Hi {data['name']}")
        
    def disconnect(self, code):
        print("disconnected with code", code)
        
        
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("async connected!")
        await self.accept()
        # await self.close()    # to forcefully disconnect the websocket
        
    async def receive(self, text_data=None, bytes_data=None):
        print("recieved from client", text_data)
        data = json.loads(text_data)
        await self.send(f"from server to client.. Hi {data['name']}")
        
    async def disconnect(self, code):
        print("disconnected with code", code)
        
        
        
class MyJsonWebsocketConsumer(JsonWebsocketConsumer):    #? no need to use of json.dumps of json.loads
    def connect(self):
        print("connected")
        self.accept()

    def receive_json(self, content, **kwargs):   #! content must be json
        print("recivieng from cleint", content)
        self.send_json(content)
        
    def disconnect(self, code):
        print("disconnected", code)