from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail
from projects.serializers.Installment_Payment.payment_related_details import PaymentRelatedDetailSerializer

class PaymentRelatedDetailViewSet(viewsets.ModelViewSet):
    queryset = PaymentRelatedDetail.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = PaymentRelatedDetailSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
