from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from planning.BudgetProgramcommittee.ThematicCommitteeProgram.models import ThematicCommitteeProgram
from planning.BudgetProgramcommittee.ThematicCommitteeProgram.serializers import ThematicCommitteeProgramSerializer
from planning.MunicipalityExecutiveOffice.PreAssemblyProject.models import PreAssemblyProject
from django.utils import timezone

class ThematicCommitteeProgramViewSet(viewsets.ModelViewSet):
    # queryset = ThematicCommitteeProgram.objects.all()
    serializer_class = ThematicCommitteeProgramSerializer
    def get_queryset(self):
        return ThematicCommitteeProgram.objects.filter(is_deleted=False)
    

    @action(detail=True, methods=['post'], url_path='submit-to-executive')
    def submit_to_executive(self, request, pk=None):
        try:
            project = self.get_object()

            # Create entry in PreAssemblyProject
            PreAssemblyProject.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका परियोजना",
                priority_no=project.priority_no,
                remarks=project.remarks,
            )

            # Soft delete current project
            project.status = "बजेट तथा कार्यक्रम तर्जुमा समितिले सिफारिस गरेका परियोजना"
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.save()

            return Response({"message": "Successfully submitted to Municipality Executive Office and soft-deleted."}, status=200)

        except ThematicCommitteeProgram.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
