from rest_framework import serializers
from projects.models.Installment_Payment.bankaccount_recommendation import BankAccountRecommendation

class BankAccountRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountRecommendation
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'status','project']

    def update(self, instance, validated_data):
        # Automatically update status if file is present
        file = validated_data.get('file', instance.file)
        instance.status = "अपलोड गरिएको" if file else ""
        return super().update(instance, validated_data)
