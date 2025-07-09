from rest_framework import viewsets
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from projects.serializers.Cost_Estimate.map_cost_estimate import MapCostEstimateSerializer
from authentication.models import VerificationLog 
from django.shortcuts import get_object_or_404
from projects.models.project import Project
class MapCostEstimateViewSet(viewsets.ModelViewSet):
    queryset = MapCostEstimate.objects.all().order_by('-date')
    serializer_class = MapCostEstimateSerializer

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
            
    # def perform_create(self, serializer):
    #     project_id = self.kwargs.get('serial_number')  
    #     project = get_object_or_404(Project, pk=project_id)
    #     serializer.save(project=project)
    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        project = get_object_or_404(Project, serial_number=serial_number)
        serializer.save(project=project)
