from rest_framework import serializers
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate

class MapCostEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapCostEstimate
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'status', 'is_verified']

    def update(self, instance, validated_data):
        file = validated_data.get('file', instance.file)
        if file:
            instance.status = "अपलोड गरिएको"
        if validated_data.get('checker') and validated_data.get('approver'):
            instance.status = "चेक जाचँको लागी पठाइएको"
            instance.is_verified = True
        return super().update(instance, validated_data)
