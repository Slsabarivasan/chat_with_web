# chatbot/consumers.py
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()  # Accept the WebSocket connection

    def disconnect(self, close_code):
        pass  # Handle disconnection

    def receive(self, text_data):
        # Echo back the message (replace with chatbot logic later)
        self.send(text_data=f"Echo: {text_data}")