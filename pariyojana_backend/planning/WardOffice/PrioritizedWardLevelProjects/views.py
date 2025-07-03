from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.WardOffice.PrioritizedWardLevelProjects.models import PrioritizedWardLevelProject
from planning.BudgetProgramcommittee.WardLevelProgram.models import BudgetProgramCommitteeWardLevelProgram
from planning.WardOffice.PrioritizedWardLevelProjects.serializers import PrioritizedWardLevelProjectSerializer

class PrioritizedWardLevelProjectViewSet(viewsets.ModelViewSet):
    queryset = PrioritizedWardLevelProject.objects.all()
    serializer_class = PrioritizedWardLevelProjectSerializer

    @action(detail=True, methods=['post'], url_path='recommend-to-budget-committee')
    def recommend_to_budget_committee(self, request, pk=None):
        try:
            prioritized_project = self.get_object()

            BudgetProgramCommitteeWardLevelProgram.objects.create(
                plan_name=prioritized_project.plan_name,
                thematic_area=prioritized_project.thematic_area,
                sub_area=prioritized_project.sub_area,
                source=prioritized_project.source,
                expenditure_center=prioritized_project.expenditure_center,
                budget=prioritized_project.budget,
                ward_no=prioritized_project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको वडा स्तरीय परियोजना",
                priority_no=prioritized_project.priority_no,
                remarks=prioritized_project.remarks,
            )

            # Update status in current model
            prioritized_project.status = "बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको वडा स्तरीय परियोजना"
            prioritized_project.save()

            return Response({"message": "Recommended to budget committee successfully."}, status=status.HTTP_200_OK)
        except PrioritizedWardLevelProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
