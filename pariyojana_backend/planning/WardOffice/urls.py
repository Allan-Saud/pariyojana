from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.WardOffice.WardLevelProject.views import WardLevelProjectViewSet
from planning.WardOffice.PrioritizedWardLevelProjects.views import PrioritizedWardLevelProjectViewSet
from planning.WardOffice.PrioritizedWardLevelThematic.views import PrioritizedWardLevelThematicProjectViewSet
from planning.WardOffice.MunicipalityLevelProject.views import MunicipalityLevelProjectViewSet
from planning.WardOffice.WardThematicCommitteeProjects.views import WardThematicCommitteeProjectViewSet
from planning.WardOffice.reports.wardlevelproject import DoughnutChartData
router = DefaultRouter()

# router.register(r'ward-projects', WardLevelProjectViewSet)
router.register(r'ward-projects', WardLevelProjectViewSet, basename='wardproject')
router.register(r'ward-thematic-projects', WardThematicCommitteeProjectViewSet, basename='wardthematicproject')
router.register(r'prioritized-ward-projects', PrioritizedWardLevelProjectViewSet, basename='prioritized-wardlevel-project')
router.register(r'prioritized-ward-thematic', PrioritizedWardLevelThematicProjectViewSet, basename='prioritized-wardlevel-thematic')
router.register(r'municipality-projects', MunicipalityLevelProjectViewSet,basename='municipality-projects')







urlpatterns = [
    path('', include(router.urls)),
    path('wardlevel-chart/', DoughnutChartData.as_view(), name='wardlevelchart'),
    path('wardlevelthemtic-chart/', DoughnutChartData.as_view(), name='wardlevelthematicchart'),
    path('municipalitylevel-chart/', DoughnutChartData.as_view(), name='municipalitylevelchart'),
    path('prioritizedward-chart/', DoughnutChartData.as_view(), name='prioritizedwardchart'),
    path('prioritizedwardthematic-chart/', DoughnutChartData.as_view(), name='prioritizedwardthematicchart'),
    
    
    
]
