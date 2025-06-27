from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from projects.models.project_aggrement_details import ProjectAgreementDetails
from projects.serializers.project_aggrement_details import ProjectAgreementDetailsSerializer

class ProjectAgreementDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProjectAgreementDetails.objects.all()
    serializer_class = ProjectAgreementDetailsSerializer
    permission_classes = [IsAuthenticated]

    # Optional: filter by project query param
    def get_queryset(self):
        qs = super().get_queryset()
        project_id = self.request.query_params.get('project')
        if project_id:
            qs = qs.filter(project_id=project_id)
        return qs
