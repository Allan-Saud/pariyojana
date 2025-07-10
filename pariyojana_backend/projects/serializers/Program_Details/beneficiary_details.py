from rest_framework import serializers
from projects.models.Program_Details.beneficiary_details import BeneficiaryDetail


class BeneficiaryDetailSerializer(serializers.ModelSerializer):
    female = serializers.IntegerField(required=False, allow_null=False, default=0)
    male = serializers.IntegerField(required=False, allow_null=False, default=0)
    other = serializers.IntegerField(required=False, allow_null=False, default=0)

    class Meta:
        model = BeneficiaryDetail
        fields = '__all__'
