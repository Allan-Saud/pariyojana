from rest_framework import viewsets
from project_settings.models.source import Source
from project_settings.serializers.source import SourceSerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
