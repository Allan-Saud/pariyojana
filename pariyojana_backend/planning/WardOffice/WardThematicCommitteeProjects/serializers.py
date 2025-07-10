from rest_framework import serializers
from planning.WardOffice.WardThematicCommitteeProjects.models import WardThematicCommitteeProject

class WardThematicCommitteeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardThematicCommitteeProject
        fields = '__all__'
