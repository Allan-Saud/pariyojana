from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.views import PreAssemblyProjectViewSet
from planning.MunicipalityExecutiveOffice.reports.councilSubmittedProjects import CouncilSubmittedProjectChart
from planning.MunicipalityExecutiveOffice.reports.PreAssembly import PreAssemblyProjectChart


router = DefaultRouter()
router.register(r'pre-assembly-projects', PreAssemblyProjectViewSet,basename="pre-assembly-projects")

urlpatterns = [
    path('', include(router.urls)),
     path('preassembly-chart/', PreAssemblyProjectChart.as_view(), name='wardlevelchart'),
    path('councilsubmitted-chart/', CouncilSubmittedProjectChart.as_view(), name='wardlevelthematicchart'),
]
