
from rest_framework import serializers
from django.db.models import Sum
from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail

class PaymentRelatedDetailSerializer(serializers.ModelSerializer):
    agreement_amount = serializers.SerializerMethodField()
    uploaded_file = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = PaymentRelatedDetail
        fields = (
            'id', 
            'title',
            'issue_date',
            'amount_paid',
            'payment_percent',
            'physical_progress',
            'is_active',
            'created_at',
            'updated_at',
            'uploaded_file',
            'deleted_at',
            'agreement_amount' 
        )
        read_only_fields = ['payment_percent', 'project','created_at', 'updated_at', 'deleted_at', 'agreement_amount']

    def get_agreement_amount(self, obj):
        agreement = getattr(obj.project, 'agreement_details', None)
        if agreement and hasattr(agreement, 'agreement_amount'):
            return agreement.agreement_amount
        return None

    def validate(self, attrs):
        project = self.context.get('project')
        if not project:
            raise serializers.ValidationError("Project context missing.")

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

