from rest_framework import serializers
from projects.models.Program_Details.program_detail import ProgramDetail

class ProgramDetailSerializer(serializers.ModelSerializer):
    estimated_cost = serializers.ReadOnlyField()
    contingency_amount = serializers.ReadOnlyField()
    agreement_date = serializers.ReadOnlyField()
    start_date = serializers.ReadOnlyField()
    completion_date = serializers.ReadOnlyField()
    agreement_amount = serializers.ReadOnlyField()
    public_participation_amount = serializers.ReadOnlyField()

    class Meta:
        model = ProgramDetail
        fields = [
            'id',
            'estimated_cost',
            'contingency_amount',
            'agreement_date',
            'start_date',
            'completion_date',
            'agreement_amount',
            'public_participation_amount',
        ]
