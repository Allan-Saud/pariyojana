from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
from projects.serializers.Project_Aggrement.project_aggrement_details import ProjectAgreementDetailsSerializer
from rest_framework.exceptions import ValidationError
from projects.models.project import Project
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
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
        
        
    def partial_update(self, request, *args, **kwargs):
        serial_number = kwargs.get('serial_number')
        pk = kwargs.get('pk') 

        if not serial_number:
            return Response({"detail": "Project serial_number is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not pk:
            return Response({"detail": "Agreement detail id (pk) is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = ProjectAgreementDetails.objects.get(pk=pk, project__serial_number=serial_number)
        except ProjectAgreementDetails.DoesNotExist:
            raise NotFound(f"Agreement details not found for project {serial_number} and id {pk}")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

#/5/project-agreement-details/ get and post
#  http://127.0.0.1:8000/api/projects/5/project-agreement-details/3/