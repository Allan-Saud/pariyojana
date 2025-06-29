from rest_framework import viewsets
from projects.models.progress_stage import ProjectProgress
from projects.serializers.progress_stage import ProjectProgressSerializer

# projects/views/progress_stage.py

from projects.models.project import Project

class ProjectProgressViewSet(viewsets.ModelViewSet):
    queryset = ProjectProgress.objects.all()
    serializer_class = ProjectProgressSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get("project_id")
        serial_number = self.request.query_params.get("serial_number")

        if serial_number:
            try:
                project = Project.objects.get(serial_number=serial_number)
                return self.queryset.filter(project=project).order_by('id')
            except Project.DoesNotExist:
                return ProjectProgress.objects.none()

        if project_id:
            return self.queryset.filter(project_id=project_id).order_by('id')

        return self.queryset.none()

