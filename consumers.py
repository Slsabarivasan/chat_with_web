# chatbot/consumers.py
from channels.generic.websocket import WebsocketConsumer # type: ignore

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()  # Accept the WebSocket connection

    def disconnect(self, close_code):
        pass  # Handle disconnection

    def receive(self, text_data):
        # Echo back the message (replace with chatbot logic later)
        self.send(text_data=f"Echo: {text_data}")



        # 1a44b32a413ec5fc7cbe06bea6730695 key in render.com
        # Static Outbound IP Addresses
        # 35.160.120.126
        # 44.233.151.27
        # 34.211.200.85
        # https://chat-with-web-gl1v.onrender.com link for project