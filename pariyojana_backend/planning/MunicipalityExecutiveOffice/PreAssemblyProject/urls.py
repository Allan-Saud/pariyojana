from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.views import PreAssemblyProjectViewSet

router = DefaultRouter()
router.register(r'pre-assembly-projects', PreAssemblyProjectViewSet,basename="preassembly")

urlpatterns = [
    path('', include(router.urls)),
]
