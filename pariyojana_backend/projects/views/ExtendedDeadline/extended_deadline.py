# views/extended_deadline_views.py
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
from projects.models.ExtendedDeadline.extended_deadline import ExtendedDeadline
from projects.serializers.ExtendedDeadline.extended_deadline import ExtendedDeadlineSerializer
from rest_framework import viewsets, permissions


class ExtendedDeadlineViewSet(viewsets.ModelViewSet):
    queryset = ExtendedDeadline.objects.all().order_by('-created_at')
    serializer_class = ExtendedDeadlineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project_id')
        if project_id:
            queryset = queryset.filter(agreement__project__id=project_id)
        return queryset
