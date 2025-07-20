# notifications/views.py

from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.order_by('-created_at')
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
