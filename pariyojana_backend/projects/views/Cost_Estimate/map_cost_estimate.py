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
        existing_map = {obj.title: obj for obj in existing_records}

        # Build a list with serial_no and title from your DOCUMENT_CHOICES
        document_list = [
            {"serial_no": idx + 1, "title": title_value}
            for idx, (title_value, _) in enumerate(MapCostEstimate.DOCUMENT_CHOICES)
        ]

        response_list = []

        for item in document_list:
            serial_no = item["serial_no"]
            title = item["title"]

            instance = existing_map.get(title)

            if instance:
                serializer = self.get_serializer(instance)
                data = serializer.data
            else:
                data = {
                    "id": None,
                    "project": project.pk,
                    "title": title,
                    "date": None,
                    "file": None,
                    "remarks": None,
                    "status": None,
                    "checker": None,
                    "approver": None,
                    "is_verified": False,
                    "is_active": True,
                    "created_at": None,
                    "updated_at": None,
                }

            data["serial_no"] = serial_no  

            response_list.append(data)

        return Response(response_list)




