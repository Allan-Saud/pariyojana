from rest_framework import serializers
from project_settings.models.expenditure_center import ExpenditureCenter

class ExpenditureCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureCenter
        fields = '__all__'
