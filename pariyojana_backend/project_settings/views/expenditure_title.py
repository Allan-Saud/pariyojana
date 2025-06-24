from rest_framework import viewsets
from project_settings.models.expenditure_title import ExpenditureTitle
from project_settings.serializers.expenditure_title import ExpenditureTitleSerializer

class ExpenditureTitleViewSet(viewsets.ModelViewSet):
    queryset = ExpenditureTitle.objects.all()
    serializer_class = ExpenditureTitleSerializer
