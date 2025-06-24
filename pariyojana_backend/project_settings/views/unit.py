from rest_framework import viewsets
from project_settings.models.unit import Unit
from project_settings.serializers.unit import UnitSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
