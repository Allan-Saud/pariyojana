# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import BudgetProgramWardLevelProject
# from .serializers import BudgetProgramWardLevelProjectSerializer
# from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import ExecutivePreAssemblyProject

# class BudgetProgramWardLevelProjectViewSet(viewsets.ModelViewSet):
#     queryset = BudgetProgramWardLevelProject.objects.all()
#     serializer_class = BudgetProgramWardLevelProjectSerializer

#     @action(detail=True, methods=['post'], url_path='submit-to-executive')
#     def submit_to_executive(self, request, pk=None):
#         instance = self.get_object()
#         ExecutivePreAssemblyProject.objects.create(
#             plan_name=instance.plan_name,
#             thematic_area=instance.thematic_area,
#             sub_area=instance.sub_area,
#             source=instance.source,
#             expenditure_center=instance.expenditure_center,
#             budget=instance.budget,
#             ward_no=instance.ward_no,
#             status="बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका परियोजना",
#             priority_no=instance.priority_no,
#             remarks=instance.remarks
#         )
#         return Response({"message": "Submitted to Executive Office."})


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.BudgetProgramcommittee.WardLevelProgram.models import BudgetProgramCommitteeWardLevelProgram
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from .serializers import BudgetProgramCommitteeWardLevelProgramSerializer

class BudgetProgramCommitteeWardLevelProgramViewSet(viewsets.ModelViewSet):
    queryset = BudgetProgramCommitteeWardLevelProgram.objects.all()
    serializer_class = BudgetProgramCommitteeWardLevelProgramSerializer

    @action(detail=True, methods=['post'], url_path='recommend-to-municipality-executive')
    def recommend_to_municipality_executive(self, request, pk=None):
        try:
            current_project = self.get_object()

            # Transfer the data to PreAssemblyProject
            PreAssemblyProject.objects.create(
                plan_name=current_project.plan_name,
                thematic_area=current_project.thematic_area,
                sub_area=current_project.sub_area,
                source=current_project.source,
                expenditure_center=current_project.expenditure_center,
                budget=current_project.budget,
                ward_no=current_project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका परियोजना",
                priority_no=current_project.priority_no,
                remarks=current_project.remarks,
            )

            # Update status on current project
            current_project.status = "बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका परियोजना"
            current_project.save()

            return Response({"message": "Project forwarded to municipality executive office."}, status=200)

        except BudgetProgramCommitteeWardLevelProgram.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
