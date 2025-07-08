from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.WardOffice.MunicipalityLevelProject.models import MunicipalityLevelProject
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.models import MunicipalityLevelProgram
from planning.WardOffice.MunicipalityLevelProject.serializers import MunicipalityLevelProjectSerializer
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.serializers import MunicipalityLevelProgramSerializer
from django.utils import timezone
class MunicipalityLevelProjectViewSet(viewsets.ModelViewSet):
    # queryset = MunicipalityLevelProject.objects.all()
    serializer_class = MunicipalityLevelProjectSerializer
    def get_queryset(self):
        return MunicipalityLevelProject.objects.filter(is_deleted=False)

    @action(detail=True, methods=['post'], url_path='recommend-to-budget-committee')
    def recommend_to_budget_committee(self, request, pk=None):
        try:
            project = self.get_object()

            MunicipalityLevelProgram.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको नगर स्तरीय परियोजना",
                priority_no=project.priority_no,
                remarks=project.remarks
            )

            # Soft delete the original project
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.status = "बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको नगर स्तरीय परियोजना"
            project.save()

            return Response({"message": "Project sent to budget committee and soft-deleted."}, status=200)

        except MunicipalityLevelProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)





