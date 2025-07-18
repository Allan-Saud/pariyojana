from rest_framework import viewsets
from projects.workingProgress.models.WorkProgress import WorkProgress
from .serializers import WorkProgressSerializer
from projects.models.project import Project

class WorkProgressViewSet(viewsets.ModelViewSet):
    serializer_class = WorkProgressSerializer
    
    def get_queryset(self):
        project_serial = self.kwargs.get('serial_number')
        return WorkProgress.objects.filter(project__serial_number=project_serial)
    
    def perform_create(self, serializer):
        project_serial = self.kwargs.get('serial_number')
        project = Project.objects.get(serial_number=project_serial)
        serializer.save(project=project)
