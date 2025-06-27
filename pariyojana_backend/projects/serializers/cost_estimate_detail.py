# projects/serializers/cost_estimate_detail.py

from rest_framework import serializers
from projects.models.cost_estimate_detail import CostEstimateDetail

class CostEstimateDetailSerializer(serializers.ModelSerializer):
    allocated_budget = serializers.SerializerMethodField()  # from related project

    class Meta:
        model = CostEstimateDetail
        fields = [
            'id',
            'project',
            'allocated_budget',        # Fetched from project
            'estimated_cost',
            'contingency_percent',
            'contingency_amount',
            'total_estimated_cost',
        ]
        read_only_fields = [
            'allocated_budget',
            'contingency_amount',
            'total_estimated_cost',
        ]

    def get_allocated_budget(self, obj):
        return obj.project.budget if obj.project else 0.00

