from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.WardOffice.views import WardLevelProjectViewSet
from planning.WardOffice.PrioritizedWardLevelProjects.views import PrioritizedWardLevelProjectViewSet
from planning.WardOffice.MunicipalityLevelProject.views import MunicipalityLevelProjectViewSet



router = DefaultRouter()

router.register(r'ward-projects', WardLevelProjectViewSet)
router.register(r'prioritized-ward-projects', PrioritizedWardLevelProjectViewSet)
router.register(r'municipality-projects', MunicipalityLevelProjectViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
