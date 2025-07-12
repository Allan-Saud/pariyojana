from rest_framework import serializers
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from rest_framework.exceptions import ValidationError
class MapCostEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapCostEstimate
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'status', 'is_verified','project']
        
    def create(self, validated_data):
        file = validated_data.get("file")
        if file:
            validated_data["status"] = "अपलोड गरिएको"
        return super().create(validated_data)

    def update(self, instance, validated_data):
        file = validated_data.get('file', instance.file)
        checker = validated_data.get('checker')
        approver = validated_data.get('approver')
    
         # Step 1: If no file is uploaded but checker/approver is set, raise error
        if not file and (checker or approver):
            raise ValidationError("फाइल अपलोड नगरि चेक/अप्रुभर राख्न मिल्दैन।")

        # Step 2: If file uploaded for the first time, set status
        if file and not instance.file:
            instance.status = "अपलोड गरिएको"

        # Step 3: If file already exists, and both checker and approver are being set
        if file and checker and approver:
            instance.status = "चेक जाँचको लागी पठाइएको"
            instance.is_verified = True

        return super().update(instance, validated_data)
