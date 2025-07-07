# projects/serializers/cost_estimate_detail.py

from rest_framework import serializers
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail

class CostEstimateDetailSerializer(serializers.ModelSerializer):
    allocated_budget = serializers.SerializerMethodField()  

    class Meta:
        model = CostEstimateDetail
        fields = [
            'id',
          
            'allocated_budget',      
            'estimated_cost',
            'contingency_percent',
            'contingency_amount',
            'total_estimated_cost',
        ]
        read_only_fields = [
            'allocated_budget',
            ' project',
            'contingency_amount',
            'total_estimated_cost',
        ]

    def get_allocated_budget(self, obj):
        return obj.project.budget if obj.project else 0.00

