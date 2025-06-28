from rest_framework import serializers
from projects.models.Program_Details.beneficiary_details import BeneficiaryDetail


class BeneficiaryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiaryDetail
        fields = '__all__'
