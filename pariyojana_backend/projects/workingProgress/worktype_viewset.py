from rest_framework import viewsets
from projects.workingProgress.models.WorkType import WorkType
from projects.workingProgress.serializers import WorkTypeSerializer
from projects.models.project import Project
from rest_framework.exceptions import NotFound

class WorkTypeViewSet(viewsets.ModelViewSet):
    serializer_class = WorkTypeSerializer

    def get_queryset(self):
        project_serial = self.kwargs.get('serial_number')
        return WorkType.objects.filter(project__serial_number=project_serial)

    def perform_create(self, serializer):
        project_serial = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=project_serial)
        except Project.DoesNotExist:
            raise NotFound('Project not found.')
        serializer.save(project=project)
