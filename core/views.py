from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Count

from notifications.models import PushNotification
from utils.globals import BASE_CONTEXT

# Create your views here.


def proxy_home(request):
    template_name = 'core/home.html'
    context = BASE_CONTEXT
    
    context.update({
        'room_name': request.user.id
    })
    
    if not request.user.is_anonymous:
        notification_count = PushNotification.objects.filter(user=request.user, is_read=False) \
            .aggregate(Count('id'))['id__count']
        context.update({
            'notification_count': notification_count
        })
    
    response = render(request, template_name, context)
    return response
