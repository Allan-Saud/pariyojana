from rest_framework import serializers
from .models import BudgetProgramMunicipalityPrideProgram

class BudgetProgramMunicipalityPrideProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetProgramMunicipalityPrideProgram
        fields = '__all__'
