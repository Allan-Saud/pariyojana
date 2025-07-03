from rest_framework import serializers
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject

class CouncilSubmittedProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilSubmittedProject
        fields = '__all__'
