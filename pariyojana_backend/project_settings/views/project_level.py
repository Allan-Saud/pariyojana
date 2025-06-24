from rest_framework import viewsets
from project_settings.models.project_level import ProjectLevel
from project_settings.serializers.project_level import ProjectLevelSerializer

class ProjectLevelViewSet(viewsets.ModelViewSet):
    queryset = ProjectLevel.objects.all()
    serializer_class = ProjectLevelSerializer
