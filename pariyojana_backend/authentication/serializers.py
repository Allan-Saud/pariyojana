
from rest_framework import serializers
from authentication.models import VerificationLog 

class VerificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationLog
        fields = '__all__'
