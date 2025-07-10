

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.MunicipalityPrideProject.views import MunicipalityPrideProjectViewSet

router = DefaultRouter()
router.register('municipality-pride-projects', MunicipalityPrideProjectViewSet,basename='municipalprideproject')

urlpatterns = [
    path('', include(router.urls)),
]
