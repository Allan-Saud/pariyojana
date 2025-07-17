# views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from planning.MunicipalAssembly.SubmittedProjects.models import SubmittedProjects
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.serializers import PreAssemblyProjectSerializer
from django.utils import timezone

class PreAssemblyProjectViewSet(viewsets.ModelViewSet):
    # queryset = PreAssemblyProject.objects.all()
    serializer_class = PreAssemblyProjectSerializer
    def get_queryset(self):
        return PreAssemblyProject.objects.filter(is_deleted=False)

    def _copy_project_to(self, model_class, project):
        """
        Reusable method to copy project data into another model.
        """
        return model_class.objects.create(
            plan_name=project.plan_name,
            thematic_area=project.thematic_area,
            sub_area=project.sub_area,
            source=project.source,
            expenditure_center=project.expenditure_center,
            budget=project.budget,
            ward_no=project.ward_no,
            status="नगर सभा सिफारिस भएको परियोजना",
            priority_no=project.priority_no,
            remarks=project.remarks,
        )
    @action(detail=True, methods=['post'], url_path='submit-to-assembly')
    def submit_to_assembly(self, request, pk=None):
        try:
            project = self.get_object()

            # Copy data to both models
            self._copy_project_to(SubmittedProjects, project)
            self._copy_project_to(CouncilSubmittedProject, project)

            # Soft delete the current project
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.save()

            return Response({"message": "Project submitted to assembly and soft-deleted from pre-assembly list."}, status=200)

        except PreAssemblyProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)


    @action(detail=True, methods=['post'], url_path='submit-to-council')
    def submit_to_council(self, request, pk=None):
        try:
            project = self.get_object()

            self._copy_project_to(SubmittedProjects, project)
            self._copy_project_to(CouncilSubmittedProject, project)

            project.status = "नगर सभा सिफारिस भएको परियोजना"
            project.save()

            return Response({"message": "Submitted to Council & listed successfully."}, status=200)

        except PreAssemblyProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
