from rest_framework import serializers
from project_settings.models.thematic_area import ThematicArea

class ThematicAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = '__all__'
