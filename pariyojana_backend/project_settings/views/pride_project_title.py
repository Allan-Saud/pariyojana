from rest_framework import viewsets
from project_settings.models.pride_project_title import PrideProjectTitle
from project_settings.serializers.pride_project_title import PrideProjectTitleSerializer

class PrideProjectTitleViewSet(viewsets.ModelViewSet):
    queryset = PrideProjectTitle.objects.all()
    serializer_class = PrideProjectTitleSerializer
