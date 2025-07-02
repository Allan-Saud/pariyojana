from rest_framework import serializers
from planning.PlanEntry.models import PlanEntry

class PlanEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntry
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']

    def validate(self, data):
        # If feasibility_study is 'भएको', file must be uploaded
        if data.get("feasibility_study") == "भएको" and not data.get("feasibility_file"):
            raise serializers.ValidationError({"feasibility_file": "File is required if feasibility study is 'भएको'."})
        if data.get("detailed_study") == "भएको" and not data.get("detailed_file"):
            raise serializers.ValidationError({"detailed_file": "File is required if detailed study is 'भएको'."})
        if data.get("environmental_study") == "भएको" and not data.get("environmental_file"):
            raise serializers.ValidationError({"environmental_file": "File is required if environmental study is 'भएको'."})
        return data
    



