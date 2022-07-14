from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel
from utils.globals import MAX_LENGTH

# Create your models here.


class PushNotification(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='유저')
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='제목')
    message = models.TextField(verbose_name='메시지')
    is_read = models.BooleanField(default=False, verbose_name='확인여부')
    is_delete = models.BooleanField(default=False, verbose_name='삭제여부')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = '푸시알림'
        db_table = 'pushnotifications'
    
    def __str__(self):
        return str(self.id)
