from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
from projects.serializers.Project_Aggrement.project_aggrement_details import ProjectAgreementDetailsSerializer
from rest_framework.exceptions import ValidationError
from projects.models.project import Project

class ProjectAgreementDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProjectAgreementDetails.objects.all()
    serializer_class = ProjectAgreementDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        # Try to get from nested URL param first
        serial_number = self.kwargs.get('serial_number')

        # fallback to query param if nested param not present
        if not serial_number:
            serial_number = self.request.query_params.get('project')

        if serial_number:
            qs = qs.filter(project__serial_number=serial_number)

        return qs

    def perform_create(self, serializer):
        # same logic: check nested first, then query param
        serial_number = self.kwargs.get('serial_number') or self.request.query_params.get('project')

        if not serial_number:
            raise ValidationError({"detail": "Project 'serial_number' is required as query param or URL param."})

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={serial_number} not found."})

        if ProjectAgreementDetails.objects.filter(project=project).exists():
            raise ValidationError({"detail": f"Agreement detail already exists for project {serial_number}."})

        serializer.save(project=project)
