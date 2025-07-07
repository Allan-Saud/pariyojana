# projects/views/official_detail.py

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.serializers.Consumer_Committee.official_detail import OfficialDetailSerializer
from projects.models.project import Project

class OfficialDetailViewSet(viewsets.ModelViewSet):
    queryset = OfficialDetail.objects.all().order_by('serial_no')
    serializer_class = OfficialDetailSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = super().get_queryset().order_by('serial_no')

        # Support nested route: /projects/<serial_number>/official-details/
        serial_number = self.kwargs.get('serial_number')
        if serial_number:
            queryset = queryset.filter(project__serial_number=serial_number)

        # Also support query param: ?project=6
        query_param = self.request.query_params.get('project')
        if query_param:
            queryset = queryset.filter(project__serial_number=query_param)

        return queryset

    
    def perform_create(self, serializer):
        project_sn = self.request.query_params.get('project')
        if not project_sn:
            raise Exception("Project ID (serial_number) is required in query parameters.")

        try:
            project = Project.objects.get(serial_number=project_sn)
        except Project.DoesNotExist:
            raise Exception(f"Project with serial_number={project_sn} not found.")

        serializer.save(project=project)
