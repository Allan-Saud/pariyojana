from rest_framework import serializers
from .models import PrioritizedThematicCommittee

class PrioritizedThematicCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrioritizedThematicCommittee
        fields = '__all__'
