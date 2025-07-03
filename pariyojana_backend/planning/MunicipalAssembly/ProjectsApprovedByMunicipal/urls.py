from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectsApprovedByMunicipalViewSet

router = DefaultRouter()
router.register(r'approved-projects', ProjectsApprovedByMunicipalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
