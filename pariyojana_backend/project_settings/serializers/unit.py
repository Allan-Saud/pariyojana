from rest_framework import serializers
from project_settings.models.unit import Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
