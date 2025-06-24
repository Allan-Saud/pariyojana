from rest_framework import viewsets
from project_settings.models.sub_thematic_area import SubArea
from project_settings.serializers.sub_thematic_area import SubAreaSerializer

class SubAreaViewSet(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
