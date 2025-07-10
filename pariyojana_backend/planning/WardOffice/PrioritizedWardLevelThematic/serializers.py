from rest_framework import serializers
from planning.WardOffice.PrioritizedWardLevelThematic.models import PrioritizedWardLevelThematicProject

class PrioritizedWardLevelThematicProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrioritizedWardLevelThematicProject
        fields = '__all__'
