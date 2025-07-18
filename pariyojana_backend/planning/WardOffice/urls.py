from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.WardOffice.WardLevelProject.views import WardLevelProjectViewSet
from planning.WardOffice.PrioritizedWardLevelProjects.views import PrioritizedWardLevelProjectViewSet
from planning.WardOffice.PrioritizedWardLevelThematic.views import PrioritizedWardLevelThematicProjectViewSet
from planning.WardOffice.MunicipalityLevelProject.views import MunicipalityLevelProjectViewSet
from planning.WardOffice.WardThematicCommitteeProjects.views import WardThematicCommitteeProjectViewSet
from planning.WardOffice.reports.wardlevelproject import DoughnutChartData
from planning.WardOffice.reports.municipalitylevelproject import MunicipalityLevelChartData
from planning.WardOffice.reports.prioritizedwardlevel import PrioritizedWardLevelChartData
from planning.WardOffice.reports.prioritizedwardlevelthematic import PrioritizedWardThematicChartData
from planning.WardOffice.reports.wardthematicproject import WardThematicChartData
from planning.WardOffice.reports.wardthematicproject import WardThematicCommitteeProjectDownloadReport
from planning.WardOffice.reports.wardlevelproject import WardLevelProjectDownloadReport
from planning.WardOffice.reports.prioritizedwardlevelthematic import PrioritizedWardLevelThematicProjectDownloadReport
from planning.WardOffice.reports.municipalitylevelproject import MunicipalityLevelProjectDownloadReport
from planning.WardOffice.reports.prioritizedwardlevel import PrioritizedWardLevelProjectDownloadReport



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
    path('wardlevelthemtic-chart/', WardThematicChartData.as_view(), name='wardlevelthematicchart'),
    path('municipalitylevel-chart/', MunicipalityLevelChartData.as_view(), name='municipalitylevelchart'),
    path('prioritizedward-chart/', PrioritizedWardLevelChartData.as_view(), name='prioritizedwardchart'),
    path('prioritizedwardthematic-chart/', PrioritizedWardThematicChartData.as_view(), name='prioritizedwardthematicchart'),
    
    
    path('ward-thematic/report/', WardThematicCommitteeProjectDownloadReport.as_view(), name='ward-thematic-report'),
    path('ward-level/report/', WardLevelProjectDownloadReport.as_view(), name='ward-level-report'),
    path('municipality/report/', MunicipalityLevelProjectDownloadReport.as_view(), name='municipality-report'),
    path('prioritized-wardthematic/report/', PrioritizedWardLevelThematicProjectDownloadReport.as_view(), name='prioritized-ward-thematic-report'),
    path('prioritized-ward/report/', PrioritizedWardLevelProjectDownloadReport.as_view(), name='prioritized-ward-report'),
    
    
    
]
