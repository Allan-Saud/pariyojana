# views.py — inside MunicipalAssembly/SubmittedProjects

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from planning.MunicipalAssembly.SubmittedProjects.models import SubmittedProjects
from planning.MunicipalAssembly.SubmittedProjects.serializers import SubmittedProjectsSerializer
from planning.MunicipalAssembly.ProjectsApprovedByMunicipal.models import ProjectsApprovedByMunicipal


class SubmittedProjectViewSet(viewsets.ModelViewSet):
    # queryset = SubmittedProjects.objects.all()
    serializer_class = SubmittedProjectsSerializer
    def get_queryset(self):
        return SubmittedProjects.objects.filter(is_deleted=False)


    def _copy_to_approved(self, project):
        """Internal method to copy project data to ApprovedProjects model."""
        return ProjectsApprovedByMunicipal.objects.create(
            plan_name=project.plan_name,
            thematic_area=project.thematic_area,
            sub_area=project.sub_area,
            source=project.source,
            expenditure_center=project.expenditure_center,
            budget=project.budget,
            ward_no=project.ward_no,
            status="सभाद्वारा स्वीकृत भएको",
            priority_no=project.priority_no,
            remarks=project.remarks,
        )

    

    @action(detail=True, methods=['post'], url_path='approve')
    def approve(self, request, pk=None):
        try:
            project = self.get_object()

            self._copy_to_approved(project)

            # Soft delete the original SubmittedProjects record
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.status = "सभाद्वारा स्वीकृत भएको"
            project.save()

            return Response({"message": "Project approved, transferred and soft-deleted."}, status=200)

        except SubmittedProjects.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)

