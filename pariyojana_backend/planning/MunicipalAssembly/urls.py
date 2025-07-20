from django.urls import path, include
from rest_framework.routers import DefaultRouter

from planning.MunicipalAssembly.SubmittedProjects.views import SubmittedProjectViewSet
from planning.MunicipalAssembly.ProjectsApprovedByMunicipal.views import ProjectsApprovedByMunicipalViewSet

from planning.MunicipalAssembly.reports.SubmittedProjects import (
    SubmittedProjectsChart,
    SubmittedProjectsDownloadReport
)

from planning.MunicipalAssembly.reports.ProjectApprovedByMunicipality import (
    ProjectsApprovedByMunicipalChart,
    ProjectsApprovedByMunicipalDownloadReport
)

router = DefaultRouter()
router.register(r'submitted-projects', SubmittedProjectViewSet, basename='submitted-projects')
router.register(r'approved-projects', ProjectsApprovedByMunicipalViewSet, basename='approved-projects')

urlpatterns = [
    path('', include(router.urls)),
    path('submittedproject-chart/', SubmittedProjectsChart.as_view(), name='submittedproject-chart'),
    path('submittedproject/report/', SubmittedProjectsDownloadReport.as_view(), name='submittedproject-report'),
    path('projectapprove-chart/', ProjectsApprovedByMunicipalChart.as_view(), name='projectapprove-chart'),
    path('projectapprove/report/', ProjectsApprovedByMunicipalDownloadReport.as_view(), name='projectapprove-report'),
]
