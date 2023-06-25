from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class TradeConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("trade", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("trade", self.channel_name)

    def receive(self, text_data):
        # For example, you can broadcast the received data to all connected clients
        async_to_sync(self.channel_layer.group_send)(
            'trade',
            {
                'type': 'process_trade',
                'data': json.loads(text_data),  # Assuming the data is JSON
            }
        )
    
    def process_trade(self, event):
        self.send(text_data=json.dumps(event["data"]))