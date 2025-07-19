from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from projects.models.project import Project
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember
from projects.serializers.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMemberSerializer

class MonitoringFacilitationCommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = MonitoringFacilitationCommitteeMemberSerializer

    def get_queryset(self):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        return MonitoringFacilitationCommitteeMember.objects.filter(project=project).order_by('serial_no')

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        serializer.save(project=project)