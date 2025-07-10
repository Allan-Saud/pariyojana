
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from planning.WardOffice.WardThematicCommitteeProjects.models import WardThematicCommitteeProject
from planning.WardOffice.WardThematicCommitteeProjects.serializers import WardThematicCommitteeProjectSerializer
from planning.WardOffice.PrioritizedWardLevelThematic.models import PrioritizedWardLevelThematicProject
from planning.WardOffice.WardThematicCommitteeProjects.models import WardThematicCommitteeProject

class WardThematicCommitteeProjectViewSet(viewsets.ModelViewSet):
    serializer_class = WardThematicCommitteeProjectSerializer

    def get_queryset(self):
        return WardThematicCommitteeProject.objects.filter(is_deleted=False)

    @action(detail=True, methods=['post'], url_path='prioritize')
    def prioritize(self, request, pk=None):
        try:
            project = self.get_object()

            # Create prioritized copy
            PrioritizedWardLevelThematicProject.objects.create(
                plan_name=project.plan_name,
                thematic_area=project.thematic_area,
                sub_area=project.sub_area,
                source=project.source,
                expenditure_center=project.expenditure_center,
                budget=project.budget,
                ward_no=project.ward_no,
                status="प्राथमिकरण भएको वडास्तरीय विषयगत परियोजना",
                priority_no=project.priority_no,
                remarks=project.remarks,
            )

            # Soft delete original
            project.status = "प्राथमिकरण भएको वडास्तरीय विषयगत परियोजना"
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.save()

            return Response({"message": "Successfully prioritized and soft-deleted."}, status=status.HTTP_200_OK)

        except WardThematicCommitteeProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
