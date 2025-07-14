
from rest_framework import serializers
from authentication.models import VerificationLog 

class VerificationLogSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = VerificationLog
        fields = '__all__'
