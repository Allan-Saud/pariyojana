# projects/views/monitoring_facilitation_committee.py

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from projects.models.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember
from projects.serializers.monitoring_facilitation_committee import MonitoringFacilitationCommitteeSerializer

class MonitoringFacilitationCommitteeViewSet(viewsets.ModelViewSet):
    queryset = MonitoringFacilitationCommitteeMember.objects.all().order_by('serial_no')
    serializer_class = MonitoringFacilitationCommitteeSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        if project_id:
            return self.queryset.filter(project_id=project_id)
        return self.queryset
