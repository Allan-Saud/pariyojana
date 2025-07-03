from rest_framework import serializers
from .models import SubmittedProjects

class SubmittedProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedProjects
        fields = '__all__'
