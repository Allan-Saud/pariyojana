from rest_framework import viewsets
from project_settings.models.bank import Bank
from project_settings.serializers.bank import BankSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
