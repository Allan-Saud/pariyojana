from rest_framework import viewsets, permissions
from projects.models.Cost_Estimate.cost_estimate_revision import CostEstimateRevision
from projects.serializers.Cost_Estimate.cost_estimate_revision import CostEstimateRevisionSerializer

class CostEstimateRevisionViewSet(viewsets.ModelViewSet):
    queryset = CostEstimateRevision.objects.all().order_by('-created_at')
    serializer_class = CostEstimateRevisionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(revised_by=self.request.user)

    def get_queryset(self):
        project_id = self.request.query_params.get("project_id")
        if project_id:
            return self.queryset.filter(cost_estimate__project_id=project_id)
        return self.queryset
