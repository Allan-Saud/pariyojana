from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectsApprovedByMunicipalViewSet
from planning.MunicipalAssembly.reports.ProjectApprovedByMunicipality import ProjectsApprovedByMunicipalChart

router = DefaultRouter()
router.register(r'approved-projects', ProjectsApprovedByMunicipalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projectapprove-chart/', ProjectsApprovedByMunicipalChart.as_view(), name='projectapprove'),
    
]
