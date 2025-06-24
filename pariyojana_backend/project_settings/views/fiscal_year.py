from rest_framework import viewsets
from project_settings.models.fiscal_year import FiscalYear
from project_settings.serializers.fiscal_year import FiscalYearSerializer

class FiscalYearViewSet(viewsets.ModelViewSet):
    queryset = FiscalYear.objects.all()
    serializer_class = FiscalYearSerializer
