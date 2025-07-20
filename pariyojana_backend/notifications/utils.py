# notifications/utils.py

from notifications.models import Notification

def create_notification(message, user=None):
    Notification.objects.create(message=message, created_by=user)
