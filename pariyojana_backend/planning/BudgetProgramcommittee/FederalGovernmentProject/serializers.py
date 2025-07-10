from rest_framework import serializers
from .models import BudgetProgramFederalGovernmentProgram

class BudgetProgramFederalGovernmentProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetProgramFederalGovernmentProgram
        fields = '__all__'
