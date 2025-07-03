from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from planning.MunicipalAssembly.SubmittedProjects.models import SubmittedProjects
from planning.MunicipalAssembly.SubmittedProjects.serializers import SubmittedProjectsSerializer
from planning.MunicipalAssembly.ProjectsApprovedByMunicipal.models import ProjectsApprovedByMunicipal

class SubmittedProjectViewSet(viewsets.ModelViewSet):
    queryset = SubmittedProjects.objects.all()
    serializer_class = SubmittedProjectsSerializer

    @action(detail=True, methods=['post'], url_path='approve')
    def approve(self, request, pk=None):
        try:
            project = self.get_object()

            # Transfer the data to approved project model
            ProjectsApprovedByMunicipal.objects.create(
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

            # Update status in current model (optional)
            project.status = "सभाद्वारा स्वीकृत भएको"
            project.save()

            return Response({"message": "Project approved and transferred."}, status=200)

        except SubmittedProjects.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)



# views.py inside MunicipalAssembly/SubmittedProjects

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from planning.MunicipalAssembly.SubmittedProjects.models import SubmittedProjects
from planning.MunicipalAssembly.ProjectsApprovedByMunicipal.models import ProjectsApprovedByMunicipal
from planning.MunicipalAssembly.SubmittedProjects.serializers import SubmittedProjectsSerializer

class SubmittedProjectViewSet(viewsets.ModelViewSet):
    queryset = SubmittedProjects.objects.all()
    serializer_class = SubmittedProjectsSerializer

    @action(detail=True, methods=['post'], url_path='approve')
    def approve(self, request, pk=None):
        try:
            project = self.get_object()

            # Transfer to Approved Projects model
            ProjectsApprovedByMunicipal.objects.create(
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

            # Update original project's status (optional)
            project.status = "सभाद्वारा स्वीकृत भएको"
            project.save()

            return Response({"message": "Project approved and transferred."}, status=200)

        except SubmittedProjects.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
