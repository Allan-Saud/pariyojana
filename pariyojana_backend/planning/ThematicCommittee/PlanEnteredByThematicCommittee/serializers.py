from rest_framework import serializers
from .models import PlanEnteredByThematicCommittee

class PlanEnteredByThematicCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEnteredByThematicCommittee
        fields = '__all__'
