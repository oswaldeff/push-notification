import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.safestring import mark_safe
from django.shortcuts import render
from django.http import HttpResponse

from .models import PushNotification
from utils.globals import BASE_CONTEXT
from utils.decorators import authorization

# Create your views here.


@authorization
def notification_trigger(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notification_{request.user.id}',
        {
            'type': 'send_notification',
            'message': mark_safe(json.dumps('NEW PUSH NOTIFICATION OBJECT'))
        }
    )
    
    PushNotification.objects.create(
        user=request.user,
        title='new',
        message='This is test message'
    )
    
    BASE_CONTEXT['notification_count'] += 1
    
    return HttpResponse('Done')


@authorization
def render_notification_list(request):
    template_name = 'notifications/list.html'
    context = BASE_CONTEXT
    
    notifications = PushNotification.objects.filter(user=request.user, is_delete=False)
    notifications.update(is_read=True)
    
    context.update({
        'notifications': notifications,
        'notification_count': 0,
    })
    
    response = render(request, template_name, context)
    return response
