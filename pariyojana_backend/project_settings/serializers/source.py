from rest_framework import serializers
from project_settings.models.source import Source

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
