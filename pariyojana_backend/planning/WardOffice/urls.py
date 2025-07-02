from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.WardOffice.views import WardLevelProjectViewSet

router = DefaultRouter()
router.register(r'ward-projects', WardLevelProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
