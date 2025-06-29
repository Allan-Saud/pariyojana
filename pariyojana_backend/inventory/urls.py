
from rest_framework.routers import DefaultRouter
from .views import SupplierRegistryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'supplier-registry', SupplierRegistryViewSet, basename='supplier-registry')

urlpatterns = [
    path('', include(router.urls)),
]
