from rest_framework import viewsets
from project_settings.models.thematic_area import ThematicArea
from project_settings.serializers.thematic_area import ThematicAreaSerializer

class ThematicAreaViewSet(viewsets.ModelViewSet):
    queryset = ThematicArea.objects.all()
    serializer_class = ThematicAreaSerializer
