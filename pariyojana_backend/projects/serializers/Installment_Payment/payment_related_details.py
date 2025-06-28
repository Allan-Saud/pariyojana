# from rest_framework import serializers
# from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail
# from django.db.models import Sum

# class PaymentRelatedDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentRelatedDetail
#         fields = '__all__'
#         read_only_fields = ['payment_percent', 'created_at', 'updated_at', 'deleted_at']

#     def validate(self, attrs):
#         project = attrs.get('project')
#         amount_paid = attrs.get('amount_paid')

#         # Total agreed budget from project_agreement_details
#         agreement_amount = project.agreement_details.agreement_amount

#         # Sum of previous payments
#         previous_paid = PaymentRelatedDetail.objects.filter(project=project, is_active=True).aggregate(
#         total=Sum('amount_paid'))['total'] or 0


#         if self.instance:
#             # Editing existing record: subtract its own amount from previous
#             previous_paid -= self.instance.amount_paid

#         remaining = agreement_amount - previous_paid
#         if amount_paid > remaining:
#             raise serializers.ValidationError(f"हाल भुक्तनी गर्नुपर्ने रकम (रु. {amount_paid}) exceeds remaining amount (रु. {remaining}).")

  
#         payment_percent = (amount_paid / agreement_amount) * 100
#         attrs['payment_percent'] = round(payment_percent, 2)

#         return attrs


from rest_framework import serializers
from django.db.models import Sum
from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail

class PaymentRelatedDetailSerializer(serializers.ModelSerializer):
    agreement_amount = serializers.SerializerMethodField()

    class Meta:
        model = PaymentRelatedDetail
        fields = (
            'id',  # all your model fields listed here,
            'project',
            'title',
            'issue_date',
            'amount_paid',
            'payment_percent',
            'physical_progress',
            'is_active',
            'created_at',
            'updated_at',
            'deleted_at',
            'agreement_amount' 
        )
        read_only_fields = ['payment_percent', 'created_at', 'updated_at', 'deleted_at', 'agreement_amount']

    def get_agreement_amount(self, obj):
        agreement = getattr(obj.project, 'agreement_details', None)
        if agreement and hasattr(agreement, 'agreement_amount'):
            return agreement.agreement_amount
        return None

    def validate(self, attrs):
        project = attrs.get('project')
        amount_paid = attrs.get('amount_paid')

        agreement = getattr(project, 'agreement_details', None)
        if not agreement or not hasattr(agreement, 'agreement_amount'):
            raise serializers.ValidationError("सम्झौता रकम फेला परेन।")

        agreement_amount = agreement.agreement_amount

        previous_paid = PaymentRelatedDetail.objects.filter(project=project, is_active=True).aggregate(
            total=Sum('amount_paid')
        )['total'] or 0

        if self.instance:
            previous_paid -= self.instance.amount_paid

        remaining = agreement_amount - previous_paid

        if amount_paid > remaining:
            raise serializers.ValidationError(
                f"हाल भुक्तनी गर्नुपर्ने रकम (रु. {amount_paid}) बाँकी रकम (रु. {remaining}) भन्दा बढी हुन सक्दैन।"
            )

        payment_percent = (amount_paid / agreement_amount) * 100
        attrs['payment_percent'] = round(payment_percent, 2)

        return attrs
