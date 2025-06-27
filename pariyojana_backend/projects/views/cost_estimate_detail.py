# projects/views/cost_estimate_detail.py

from rest_framework import viewsets
from projects.models.cost_estimate_detail import CostEstimateDetail
from projects.serializers.cost_estimate_detail import CostEstimateDetailSerializer

class CostEstimateDetailViewSet(viewsets.ModelViewSet):
    queryset = CostEstimateDetail.objects.all()
    serializer_class = CostEstimateDetailSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get("project")
        if project_id:
            return self.queryset.filter(project_id=project_id)
        return self.queryset
