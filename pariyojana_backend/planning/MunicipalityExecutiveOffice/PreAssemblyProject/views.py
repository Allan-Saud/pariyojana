from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from planning.MunicipalAssembly.SubmittedProjects.models import SubmittedProjects
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject
from .serializers import PreAssemblyProjectSerializer

class PreAssemblyProjectViewSet(viewsets.ModelViewSet):
    queryset = PreAssemblyProject.objects.all()
    serializer_class = PreAssemblyProjectSerializer

    @action(detail=True, methods=['post'], url_path='submit-to-municipal-assembly')
    def submit_to_municipal_assembly(self, request, pk=None):
        try:
            project = self.get_object()

            # Step 1: Transfer to SubmittedProjects
            SubmittedProjects.objects.create(
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

            # Step 2: Also insert into CouncilSubmittedProjects
            CouncilSubmittedProject.objects.create(
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

            # Step 3: Update status of current record
            project.status = "नगर सभा सिफारिस भएको परियोजना"
            project.save()

            return Response({"message": "Successfully submitted to municipal assembly and council records."}, status=200)

        except PreAssemblyProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
        
        

# views.py (PreAssemblyProject)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from planning.MunicipalAssembly.SubmittedProjects.models import SubmittedProjects
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.serializers import PreAssemblyProjectSerializer

class PreAssemblyProjectViewSet(viewsets.ModelViewSet):
    queryset = PreAssemblyProject.objects.all()
    serializer_class = PreAssemblyProjectSerializer

    @action(detail=True, methods=['post'], url_path='submit-to-assembly')
    def submit_to_assembly(self, request, pk=None):
        try:
            project = self.get_object()

            # Create record in MunicipalAssembly SubmittedProjects
            SubmittedProjects.objects.create(
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

            # Also list in CouncilSubmittedProjects
            CouncilSubmittedProject.objects.create(
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

            # Update original PreAssemblyProject's status
            project.status = "नगर सभा सिफारिस भएको परियोजना"
            project.save()

            return Response({"message": "Project submitted to assembly and council list updated."}, status=200)

        except PreAssemblyProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)

# views.py inside MunicipalityExecutiveOffice/PreAssemblyProject/

# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
# from planning.MunicipalAssembly.ProjectsApprovedByMunicipal.models import ProjectsApprovedByMunicipal
# from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject

# from .serializers import PreAssemblyProjectSerializer


# class PreAssemblyProjectViewSet(viewsets.ModelViewSet):
#     queryset = PreAssemblyProject.objects.all()
#     serializer_class = PreAssemblyProjectSerializer

#     @action(detail=True, methods=['post'], url_path='submit-to-assembly')
#     def submit_to_assembly(self, request, pk=None):
#         try:
#             project = self.get_object()

#             # Transfer to ProjectsApprovedByMunicipal
#             ProjectsApprovedByMunicipal.objects.create(
#                 plan_name=project.plan_name,
#                 thematic_area=project.thematic_area,
#                 sub_area=project.sub_area,
#                 source=project.source,
#                 expenditure_center=project.expenditure_center,
#                 budget=project.budget,
#                 ward_no=project.ward_no,
#                 status="नगर सभा सिफारिस भएको परियोजना",
#                 priority_no=project.priority_no,
#                 remarks=project.remarks,
#             )

#             # Also list in CouncilSubmittedProjects
#             CouncilSubmittedProject.objects.create(
#                 plan_name=project.plan_name,
#                 thematic_area=project.thematic_area,
#                 sub_area=project.sub_area,
#                 source=project.source,
#                 expenditure_center=project.expenditure_center,
#                 budget=project.budget,
#                 ward_no=project.ward_no,
#                 status="नगर सभा सिफारिस भएको परियोजना",
#                 priority_no=project.priority_no,
#                 remarks=project.remarks,
#             )

#             # Update status of current model
#             project.status = "नगर सभा सिफारिस भएको परियोजना"
#             project.save()

#             return Response({"message": "Project submitted to assembly and council."}, status=200)

#         except PreAssemblyProject.DoesNotExist:
#             return Response({"error": "Project not found"}, status=404)
