from rest_framework import serializers
from planning.MunicipalityPrideProject.models import MunicipalityPrideProject

class MunicipalityPrideProjectSerializer(serializers.ModelSerializer):
    priority_no = serializers.IntegerField(required=False, min_value=1, allow_null=True)
    class Meta:
        model = MunicipalityPrideProject
        fields = '__all__'
