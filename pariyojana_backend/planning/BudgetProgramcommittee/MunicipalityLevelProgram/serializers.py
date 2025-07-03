from rest_framework import serializers
from .models import MunicipalityLevelProgram

class MunicipalityLevelProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalityLevelProgram
        fields = '__all__'
