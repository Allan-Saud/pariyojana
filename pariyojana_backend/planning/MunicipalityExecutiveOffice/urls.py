from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.views import PreAssemblyProjectViewSet
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.views import CouncilSubmittedProjectViewSet

from planning.MunicipalityExecutiveOffice.reports.councilSubmittedProjects import CouncilSubmittedProjectChart
from planning.MunicipalityExecutiveOffice.reports.PreAssembly import PreAssemblyProjectChart
from planning.MunicipalityExecutiveOffice.reports.PreAssembly import PreAssemblyProjectDownloadReport
from planning.MunicipalityExecutiveOffice.reports.councilSubmittedProjects import CouncilSubmittedProjectDownloadReport



router = DefaultRouter()
router.register(r'pre-assembly-projects', PreAssemblyProjectViewSet,basename="pre-assembly-projects")
router.register(r'council-submitted-projects', CouncilSubmittedProjectViewSet, basename="council-submitted-projects")


urlpatterns = [
    path('', include(router.urls)),
    path('preassembly-chart/', PreAssemblyProjectChart.as_view(), name='wardlevelchart'),
    path('councilsubmitted-chart/', CouncilSubmittedProjectChart.as_view(), name='wardlevelthematicchart'),
    
    path('preassembly/report', PreAssemblyProjectDownloadReport.as_view(), name='wardlevelchartreport'),
    path('councilsubmitted/report', CouncilSubmittedProjectDownloadReport.as_view(), name='wardlevelthematicchartreport'),
    
    
    
]

