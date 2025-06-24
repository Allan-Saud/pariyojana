from rest_framework import serializers
from project_settings.models.project_level import ProjectLevel

class ProjectLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLevel
        fields = '__all__'
