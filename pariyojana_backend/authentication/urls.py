from authentication.worker_views import PersonViewSet


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.worker_views import PersonViewSet  
from authentication.views import VerificationLogViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')
router.register(r'verification-logs', VerificationLogViewSet, basename='verificationlog')
urlpatterns = [
    path('', include(router.urls)),
]


