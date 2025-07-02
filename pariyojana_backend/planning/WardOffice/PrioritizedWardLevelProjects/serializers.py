from rest_framework import serializers
from planning.WardOffice.PrioritizedWardLevelProjects.models import PrioritizedWardLevelProject

class PrioritizedWardLevelProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrioritizedWardLevelProject
        fields = '__all__'
