from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmittedProjectViewSet
from planning.MunicipalAssembly.reports.SubmittedProjects import SubmittedProjectsChart

router = DefaultRouter()
router.register(r'submitted-projects', SubmittedProjectViewSet,basename='submitted-projects')

urlpatterns = [
    path('', include(router.urls)),
    path('submittedproject-chart/', SubmittedProjectsChart.as_view(), name='submittedproject'),
]
