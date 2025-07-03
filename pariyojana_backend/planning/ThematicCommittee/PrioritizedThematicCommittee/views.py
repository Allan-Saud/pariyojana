from rest_framework import viewsets
from .models import PrioritizedThematicCommittee
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PrioritizedThematicCommitteeSerializer
from planning.BudgetProgramcommittee.ThematicCommitteeProgram.models import ThematicCommitteeProgram

class PrioritizedThematicCommitteeViewSet(viewsets.ModelViewSet):
    queryset = PrioritizedThematicCommittee.objects.all()
    serializer_class = PrioritizedThematicCommitteeSerializer
    
    @action(detail=True, methods=['post'], url_path='submit-to-budget-committee')
    def submit_to_budget_committee(self, request, pk=None):
        try:
            project = self.get_object()

            # Create entry in Budget Committee model
            ThematicCommitteeProgram.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको विषयगत समितिका परियोजना",
                priority_no=project.priority_no,
                remarks=project.remarks
            )

            # Optionally update current status
            project.status = "बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको विषयगत समितिका परियोजना"
            project.save()

            return Response({"message": "Successfully submitted to Budget Committee"}, status=200)

        except PrioritizedThematicCommittee.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
