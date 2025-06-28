from rest_framework import viewsets
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from projects.serializers.Cost_Estimate.map_cost_estimate import MapCostEstimateSerializer
from authentication.models import VerificationLog 

class MapCostEstimateViewSet(viewsets.ModelViewSet):
    queryset = MapCostEstimate.objects.all().order_by('-date')
    serializer_class = MapCostEstimateSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # If verified, log it into authentication app
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
