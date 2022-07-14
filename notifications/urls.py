from django.urls import path

from .views import notification_trigger, render_notification_list

app_name = 'notifications'

urlpatterns = [
    path('trigger', notification_trigger),
    path('list', render_notification_list, name='list'),
]
