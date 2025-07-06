# from authentication.worker_views import PersonViewSet


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VerificationLogViewSet,
    check_document,
    approve_document
)

router = DefaultRouter()
router.register(r'verification-logs', VerificationLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('documents/<int:document_id>/check/', check_document, name='check-document'),
    path('documents/<int:document_id>/approve/', approve_document, name='approve-document'),
]