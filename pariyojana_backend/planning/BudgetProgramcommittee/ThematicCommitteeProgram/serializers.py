from rest_framework import serializers
from .models import ThematicCommitteeProgram

class ThematicCommitteeProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicCommitteeProgram
        fields = '__all__'
