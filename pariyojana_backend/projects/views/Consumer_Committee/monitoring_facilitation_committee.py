from rest_framework import viewsets, status
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        # Get the actual data if it exists
        queryset = self.filter_queryset(self.get_queryset())
        
        # If you want to return empty fields when no data exists
        if not queryset.exists():
            # Create an empty instance with default values
            empty_data = {
                'id': None,
                'serial_no': None,
                'post': None,
                'full_name': None,
                'gender': None,
                'address': None,
                'citizenship_no': None,
                'contact_no': None,
                'citizenship_front': None,
                'citizenship_back': None,
                'citizenship_front_url': None,
                'citizenship_back_url': None,
                'created_at': None,
                'updated_at': None
            }
            return Response([empty_data])
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            # Return empty data if instance doesn't exist
            empty_data = {
                'id': None,
                'serial_no': None,
                'post': None,
                'full_name': None,
                'gender': None,
                'address': None,
                'citizenship_no': None,
                'contact_no': None,
                'citizenship_front': None,
                'citizenship_back': None,
                'citizenship_front_url': None,
                'citizenship_back_url': None,
                'created_at': None,
                'updated_at': None
            }
            return Response(empty_data)

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise ValidationError({"detail": "Missing project serial_number in URL."})

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={serial_number} not found."})

        serializer.save(project=project)