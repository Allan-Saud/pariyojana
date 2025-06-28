from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from projects.models.Installment_Payment.bankaccount_recommendation import BankAccountRecommendation
from projects.serializers.Installment_Payment.bankaccount_recommendation import BankAccountRecommendationSerializer

class BankAccountRecommendationViewSet(viewsets.ModelViewSet):
    queryset = BankAccountRecommendation.objects.filter(is_active=True).order_by('-date')
    serializer_class = BankAccountRecommendationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
