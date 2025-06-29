
from rest_framework import serializers
from projects.models.Cost_Estimate.cost_estimate_revision import CostEstimateRevision

class CostEstimateRevisionSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True)
    project_name = serializers.CharField(source='cost_estimate.project.name', read_only=True)

    class Meta:
        model = CostEstimateRevision
        fields = [
            'id',

            # Linking to project
            'project_id',
            'project_name',

            # Previous values
            'prev_estimated_cost',
            'prev_contingency_percent',
            'prev_contingency_amount',
            'prev_total_estimated_cost',

            # Revised inputs
            'revised_estimated_cost',
            'revised_contingency_percent',
            'revised_contingency_amount',
            'revised_total_estimated_cost',

            'reason',
            'created_at'
        ]
        read_only_fields = [
            'prev_estimated_cost',
            'prev_contingency_percent',
            'prev_contingency_amount',
            'prev_total_estimated_cost',
            'revised_contingency_amount',
            'revised_total_estimated_cost',
            'created_at',
            'project_name'
        ]

    def create(self, validated_data):
        project_id = validated_data.pop('project_id')
        from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail

        try:
            cost_estimate = CostEstimateDetail.objects.get(project_id=project_id)
        except CostEstimateDetail.DoesNotExist:
            raise serializers.ValidationError("Cost estimate not found for this project.")

        return CostEstimateRevision.objects.create(
            cost_estimate=cost_estimate,
            **validated_data
        )
