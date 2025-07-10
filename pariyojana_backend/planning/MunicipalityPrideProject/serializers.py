from rest_framework import serializers
from planning.MunicipalityPrideProject.models import MunicipalityPrideProject

class MunicipalityPrideProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalityPrideProject
        fields = '__all__'
