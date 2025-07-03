from rest_framework import serializers
from .models import ProjectsApprovedByMunicipal

class ProjectsApprovedByMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsApprovedByMunicipal
        fields = '__all__'
