from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import MunicipalityPrideProject
from .serializers import MunicipalityPrideProjectSerializer

from planning.BudgetProgramcommittee.MunicipalityPrideProject.models import BudgetProgramMunicipalityPrideProgram
from planning.MunicipalityPrideProject.SubmittedProjectsToBudgetCommittee.models import SubmittedToBudgetMunicipalityPrideProject


class MunicipalityPrideProjectViewSet(viewsets.ModelViewSet):
    serializer_class = MunicipalityPrideProjectSerializer

    def get_queryset(self):
        return MunicipalityPrideProject.objects.filter(is_deleted=False)

    @action(detail=True, methods=['post'], url_path='recommend-to-budget-committee')
    def recommend_to_budget_committee(self, request, pk=None):
        try:
            project = self.get_object()

            # ✅ 1. Transfer to BudgetProgramMunicipalityPrideProgram
            BudgetProgramMunicipalityPrideProgram.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको नगरपालिका गौरवको आयोजना",
                priority_no=project.priority_no,
                remarks=project.remarks,
            )

            # ✅ 2. Log in SubmittedToBudgetMunicipalityPrideProject
            SubmittedToBudgetMunicipalityPrideProject.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिमा पेश गरिएको परियोजना",
                priority_no=project.priority_no,
                remarks=project.remarks,
            )

            # ✅ 3. Soft delete original
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.save()

            return Response(
                {"message": "Successfully recommended to budget committee, logged, and soft-deleted."},
                status=status.HTTP_200_OK
            )

        except MunicipalityPrideProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
