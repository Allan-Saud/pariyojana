from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import WardRecommendedProjects

from .serializers import WardRecommendedProjectsSerializer
# from planning.ThematicCommittee.PlanEnteredByThematicCommittee.models  import PlanEnteredByThematicCommittee
from planning.ThematicCommittee.PrioritizedThematicCommittee.models import PrioritizedThematicCommittee


class WardRecommendedProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = WardRecommendedProjectsSerializer

    def get_queryset(self):
        return WardRecommendedProjects.objects.filter(is_deleted=False)

    @action(detail=True, methods=['post'], url_path='prioritize')
    def recommend_to_thematic_committee(self, request, pk=None):
        try:
            prioritized = self.get_object()


            PrioritizedThematicCommittee.objects.create(
                plan_name=prioritized.plan_name,
                thematic_area=prioritized.thematic_area,
                sub_area=prioritized.sub_area,
                source=prioritized.source,
                expenditure_center=prioritized.expenditure_center,
                budget=prioritized.budget,
                ward_no=prioritized.ward_no,
                status="प्राथमिकरण भएको विषयगत समितिका परियोजना",
                priority_no=prioritized.priority_no,
                remarks=prioritized.remarks,
            )

            # Soft delete the prioritized entry
            prioritized.is_deleted = True
            prioritized.deleted_at = timezone.now()
            prioritized.save()

            return Response({"message": "Successfully prioritized and soft-deleted."}, status=status.HTTP_200_OK)

        except WardRecommendedProjects.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
