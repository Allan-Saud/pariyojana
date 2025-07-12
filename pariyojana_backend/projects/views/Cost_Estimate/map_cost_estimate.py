from rest_framework import viewsets
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from projects.serializers.Cost_Estimate.map_cost_estimate import MapCostEstimateSerializer
from authentication.models import VerificationLog 
from django.shortcuts import get_object_or_404
from projects.models.project import Project
from rest_framework.response import Response
from rest_framework import status

class MapCostEstimateViewSet(viewsets.ModelViewSet):
    queryset = MapCostEstimate.objects.all().order_by('-date')
    serializer_class = MapCostEstimateSerializer

    def get_project(self):
        serial_number = self.kwargs.get('serial_number')
        return get_object_or_404(Project, serial_number=serial_number)

    def perform_update(self, serializer):
        instance = serializer.save()

        
        if instance.is_verified:
            VerificationLog.objects.create(
                project=instance.project,
                file_title=instance.title,
                file_path=instance.file.url if instance.file else '',
                uploader_role="अपलोड कर्ता",
                status=instance.status,
                remarks=instance.remarks,
                checker=instance.checker,
                approver=instance.approver,
                source_model='MapCostEstimate',
                source_id=instance.id
            )
    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        project = get_object_or_404(Project, serial_number=serial_number)
        serializer.save(project=project)
    
        
        
    def list(self, request, *args, **kwargs):
        project = self.get_project()
        existing_records = self.queryset.filter(project=project)
        
        # Create a dictionary keyed by title
        existing_map = {obj.title: obj for obj in existing_records}

        response_list = []

        for title_value, title_display in MapCostEstimate.DOCUMENT_CHOICES:
            if title_value in existing_map:
                # Serialize the actual record
                serializer = self.get_serializer(existing_map[title_value])
                response_list.append(serializer.data)
            else:
                # Add a blank record for this title
                response_list.append({
                    "id": None,
                    "project": project.pk,
                    "title": title_value,
                    "date": None,
                    "file": None,
                    "remarks": None,
                    "status": "pending",
                    "checker": None,
                    "approver": None,
                    "is_verified": False,
                    "is_active": True,
                    "created_at": None,
                    "updated_at": None,
                })

        return Response(response_list)

