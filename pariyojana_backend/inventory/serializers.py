# serializers/supplier_registry.py
from rest_framework import serializers
from .models import SupplierRegistry

class SupplierRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierRegistry
        fields = '__all__'
