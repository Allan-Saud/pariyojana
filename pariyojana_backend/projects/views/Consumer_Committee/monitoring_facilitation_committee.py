from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError
from projects.models.project import Project
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember
from projects.serializers.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeSerializer

class MonitoringFacilitationCommitteeViewSet(viewsets.ModelViewSet):
    queryset = MonitoringFacilitationCommitteeMember.objects.all().order_by('serial_no')
    serializer_class = MonitoringFacilitationCommitteeSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = super().get_queryset().order_by('serial_no')

        # Support nested route: /projects/<serial_number>/monitoring-committee/
        serial_number = self.kwargs.get('serial_number')
        if serial_number:
            queryset = queryset.filter(project__serial_number=serial_number)

        # Support query param style: ?project=6
        project_serial_number = self.request.query_params.get('project')
        if project_serial_number:
            queryset = queryset.filter(project__serial_number=project_serial_number)

        return queryset


    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise ValidationError({"detail": "Missing project serial_number in URL."})

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={serial_number} not found."})

        serializer.save(project=project)
