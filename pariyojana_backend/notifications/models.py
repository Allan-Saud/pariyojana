# notifications/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message[:50]
