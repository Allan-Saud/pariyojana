from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from planning.BudgetProgramcommittee.MunicipalityPrideProject.models import BudgetProgramMunicipalityPrideProgram
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from planning.BudgetProgramcommittee.MunicipalityPrideProject.serializers import BudgetProgramMunicipalityPrideProgram
from .serializers import BudgetProgramMunicipalityPrideProgramSerializer
class BudgetProgramMunicipalityPrideProgramViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetProgramMunicipalityPrideProgramSerializer

    def get_queryset(self):
        return BudgetProgramMunicipalityPrideProgram.objects.filter(is_deleted=False)

    @action(detail=True, methods=['post'], url_path='submit-to-executive')
    def submit_to_executive(self, request, pk=None):
        try:
            project = self.get_object()

            # ✅ Transfer to PreAssemblyProject
            PreAssemblyProject.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका गौरवका आयोजना",
                priority_no=project.priority_no,
                remarks=project.remarks,
            )

            # ✅ Soft delete the original project
            project.status = "बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका गौरवका आयोजना"
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.save()

            return Response(
                {"message": "Successfully submitted to Municipality Executive Office and soft-deleted."},
                status=status.HTTP_200_OK
            )

        except BudgetProgramMunicipalityPrideProgram.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
