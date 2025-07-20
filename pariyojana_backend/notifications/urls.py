from rest_framework.routers import DefaultRouter
from notifications.views import NotificationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
