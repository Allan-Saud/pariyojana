from rest_framework import serializers
from .models import BudgetProgramCommitteeWardLevelProgram

class BudgetProgramCommitteeWardLevelProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetProgramCommitteeWardLevelProgram
        fields = '__all__'
