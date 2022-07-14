from django.contrib import admin

from notifications.models import PushNotification

# Register your models here.


@admin.register(PushNotification)
class PushNotificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'title',
        'message',
        'is_read',
        'is_delete',
        'created_at',
        'updated_at',
    ]
    
    actions = ['delete_notification']
    
    
    def delete_notification(self, request, queryset):
        queryset.update(is_delete=True)
    delete_notification.short_description = '선택된 푸시알림을 삭제합니다.'
