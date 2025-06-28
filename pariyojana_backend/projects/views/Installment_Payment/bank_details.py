from rest_framework import viewsets
from projects.models.Installment_Payment.bank_details import BankDetail
from projects.serializers.Installment_Payment.bank_details import BankDetailSerializer
from rest_framework.permissions import IsAuthenticated

class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer
    permission_classes = [IsAuthenticated]
