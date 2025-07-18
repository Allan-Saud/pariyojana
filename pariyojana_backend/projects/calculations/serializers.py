from rest_framework import serializers
from .models import CostEstimationCalculation

class CostEstimationCalculationSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.project_name', read_only=True)
    fiscal_year_display = serializers.CharField(source='fiscal_year.year', read_only=True)

    class Meta:
        model = CostEstimationCalculation
        fields = [
            'id', 'project_name',
            'fiscal_year', 'fiscal_year_display',
            'provincial_budget', 'local_budget',
            'total_without_vat', 'ps_amount',
            'vat_percent', 'vat_amount',
            'contingency_percent', 'contingency_amount',
            'grand_total', 'created_at'
        ]
        read_only_fields = ['vat_amount', 'contingency_amount', 'grand_total', 'created_at', 'project']
