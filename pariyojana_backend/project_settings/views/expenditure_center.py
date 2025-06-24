from rest_framework import viewsets
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.serializers.expenditure_center import ExpenditureCenterSerializer

class ExpenditureCenterViewSet(viewsets.ModelViewSet):
    queryset = ExpenditureCenter.objects.all()
    serializer_class = ExpenditureCenterSerializer
