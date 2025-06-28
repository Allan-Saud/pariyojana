from rest_framework import serializers
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails

class ProjectAgreementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAgreementDetails
        fields = '__all__'
        read_only_fields = [
            'cost_estimate', 'contingency_amount', 'contingency_percentage', 'total_cost_estimate',
            'municipality_percentage', 'public_participation_amount', 'public_participation_percentage',
            'created_at', 'updated_at',
        ]

    def validate(self, data):
        total_cost_estimate = data.get('total_cost_estimate') or self.instance.total_cost_estimate if self.instance else None
        agreement_amount = data.get('agreement_amount') or self.instance.agreement_amount if self.instance else None
        municipality_amount = data.get('municipality_amount') or self.instance.municipality_amount if self.instance else None

        if total_cost_estimate and agreement_amount and agreement_amount > total_cost_estimate:
            raise serializers.ValidationError({'agreement_amount': 'सम्झौता रकम cannot be greater than कुल लागत अनुमान'})

        if agreement_amount and municipality_amount and municipality_amount > agreement_amount:
            raise serializers.ValidationError({'municipality_amount': 'नगरपालिकाले ब्यहेर्ने रकम cannot be greater than सम्झौता रकम'})

        return data
