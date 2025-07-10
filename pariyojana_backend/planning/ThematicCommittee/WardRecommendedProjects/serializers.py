from rest_framework import serializers
from .models import WardRecommendedProjects

class WardRecommendedProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardRecommendedProjects
        fields = '__all__'
