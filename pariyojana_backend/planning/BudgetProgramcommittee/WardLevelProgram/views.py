from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.BudgetProgramcommittee.WardLevelProgram.models import BudgetProgramCommitteeWardLevelProgram
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from .serializers import BudgetProgramCommitteeWardLevelProgramSerializer
from django.utils import timezone
class BudgetProgramCommitteeWardLevelProgramViewSet(viewsets.ModelViewSet):
    # queryset = BudgetProgramCommitteeWardLevelProgram.objects.all()
    serializer_class = BudgetProgramCommitteeWardLevelProgramSerializer
    def get_queryset(self):
        return BudgetProgramCommitteeWardLevelProgram.objects.filter(is_deleted=False)

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

            # Soft delete the current project
            current_project.is_deleted = True
            current_project.deleted_at = timezone.now()
            current_project.save()

            return Response({"message": "Project forwarded to municipality executive office and soft-deleted."}, status=status.HTTP_200_OK)

        except BudgetProgramCommitteeWardLevelProgram.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

