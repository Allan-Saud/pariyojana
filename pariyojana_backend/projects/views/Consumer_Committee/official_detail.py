from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.serializers.Consumer_Committee.official_detail import OfficialDetailSerializer
from projects.models.project import Project
from rest_framework import viewsets
from rest_framework.exceptions import NotFound

class OfficialDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OfficialDetailSerializer

    def get_queryset(self):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise NotFound("Project not found")
        return OfficialDetail.objects.filter(project=project).order_by('serial_no')

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise NotFound("Project not found")
        serializer.save(project=project)
