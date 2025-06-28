
from rest_framework import serializers
from authentication.models import VerificationLog  # adjust model name

class VerificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationLog
        fields = '__all__'
