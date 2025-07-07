# # views/consumer_committee_details.py

from rest_framework import viewsets
from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
from projects.serializers.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from projects.models.project import Project

class ConsumerCommitteeDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumerCommitteeDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ConsumerCommitteeDetail.objects.filter(is_active=True)
        
        # Support nested URL like /projects/<serial_number>/consumer-committee-details/
        serial_number = self.kwargs.get('serial_number')
        if serial_number:
            queryset = queryset.filter(project__serial_number=serial_number)
        
        # Support old query param based filtering: ?project_id=6
        project_serial_number = self.request.query_params.get('project_id')
        if project_serial_number:
            queryset = queryset.filter(project__serial_number=project_serial_number)

        return queryset

    
    
    def perform_create(self, serializer):
        project_sn = self.request.query_params.get('project_id')
        if not project_sn:
            raise ValidationError({"detail": "Project ID (serial_number) is required as query param `project_id`."})
        
        try:
            project = Project.objects.get(serial_number=project_sn)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={project_sn} not found."})

        serializer.save(project=project)