from rest_framework import serializers
from .models import ProvinciallytransferredProgram

class ProvinciallytransferredProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinciallytransferredProgram
        fields = '__all__'
