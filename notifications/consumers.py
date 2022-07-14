import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.user = self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_room_name = f'notification_{self.user}'
        
        await self.channel_layer.group_add( # Join room group
            self.user_room_name,
            self.channel_name
        )
        
        await self.accept()
    
    
    async def disconnect(self, close_code):
        '''
        Leave room group
        '''
        await self.channel_layer.group_discard(
            self.user_room_name,
            self.channel_name
        )
    
    
    # async def receive(self, text_data):
    #     '''
    #     Receive message from WebSocket
    #     '''
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
        
    #     await self.channel_layer.group_send( # Send message to room group
    #         self.user_room_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )
    
    async def send_notification(self, event):
        '''
        Receive message from room group
        '''
        message = event['message']
        
        await self.send(text_data=json.dumps(message)) # Send message to WebSocket
