from rest_framework import serializers
from project_settings.models.fiscal_year import FiscalYear

class FiscalYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYear
        fields = '__all__'
        extra_kwargs = {
            'year': {'required': False, 'allow_null': True, 'allow_blank': True},
        }
