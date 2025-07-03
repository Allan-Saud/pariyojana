from rest_framework import serializers
from planning.WardOffice.MunicipalityLevelProject.models import MunicipalityLevelProject

class MunicipalityLevelProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalityLevelProject
        fields = '__all__'
