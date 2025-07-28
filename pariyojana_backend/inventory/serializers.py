# # # serializers/supplier_registry.py
# # from rest_framework import serializers
# # from .models import SupplierRegistry

# # class SupplierRegistrySerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = SupplierRegistry
# #         fields = '__all__'


# from rest_framework import serializers
# from .models import SupplierRegistry

# class SupplierRegistrySerializer(serializers.ModelSerializer):
#     registration_certificate_file = serializers.FileField(use_url=True, required=False)
#     license_file = serializers.FileField(use_url=True, required=False)
#     tax_clearance_file = serializers.FileField(use_url=True, required=False)
#     pan_file = serializers.FileField(use_url=True, required=False)

#     class Meta:
#         model = SupplierRegistry
#         fields = '__all__'
# serializers/supplier_registry.py
from rest_framework import serializers
from .models import SupplierRegistry

class SupplierRegistrySerializer(serializers.ModelSerializer):
    registration_certificate_file = serializers.FileField(use_url=True, required=False)
    license_file = serializers.FileField(use_url=True, required=False)
    tax_clearance_file = serializers.FileField(use_url=True, required=False)
    pan_file = serializers.FileField(use_url=True, required=False)
    existing_inventory_list = serializers.FileField(use_url=True, required=False)  # ✅ added

    class Meta:
        model = SupplierRegistry
        fields = '__all__'
