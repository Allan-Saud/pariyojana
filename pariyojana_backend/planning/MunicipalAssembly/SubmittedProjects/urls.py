from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmittedProjectViewSet

router = DefaultRouter()
router.register(r'submitted-projects', SubmittedProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
