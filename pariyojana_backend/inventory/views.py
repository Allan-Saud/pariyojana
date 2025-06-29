# views/supplier_registry.py
from rest_framework import viewsets, permissions
from .models import SupplierRegistry
from .serializers import SupplierRegistrySerializer

class SupplierRegistryViewSet(viewsets.ModelViewSet):
    queryset = SupplierRegistry.objects.all().order_by('-created_at')
    serializer_class = SupplierRegistrySerializer
    permission_classes = [permissions.IsAuthenticated]
