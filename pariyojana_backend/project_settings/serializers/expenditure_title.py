from rest_framework import serializers
from project_settings.models.expenditure_title import ExpenditureTitle

class ExpenditureTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureTitle
        fields = '__all__'
