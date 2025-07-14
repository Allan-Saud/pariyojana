from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectsApprovedByMunicipalViewSet
from planning.MunicipalAssembly.reports.ProjectApprovedByMunicipality import ProjectsApprovedByMunicipalChart
from planning.MunicipalAssembly.reports.ProjectApprovedByMunicipality import ProjectsApprovedByMunicipalDownloadReport

router = DefaultRouter()
router.register(r'approved-projects', ProjectsApprovedByMunicipalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projectapprove-chart/', ProjectsApprovedByMunicipalChart.as_view(), name='projectapprove'),
    
    path('projectapprove/report', ProjectsApprovedByMunicipalDownloadReport.as_view(), name='projectapprovereport'),
    
]
