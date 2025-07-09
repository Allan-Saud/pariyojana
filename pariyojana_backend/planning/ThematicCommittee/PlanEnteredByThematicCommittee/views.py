from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PlanEnteredByThematicCommittee
from .serializers import PlanEnteredByThematicCommitteeSerializer
from django.utils import timezone
from planning.ThematicCommittee.PrioritizedThematicCommittee.models import PrioritizedThematicCommittee

class PlanEnteredByThematicCommitteeViewSet(viewsets.ModelViewSet):
    # queryset = PlanEnteredByThematicCommittee.objects.all()
    serializer_class = PlanEnteredByThematicCommitteeSerializer
    def get_queryset(self):
        return PlanEnteredByThematicCommittee.objects.filter(is_deleted=False)


    # @action(detail=True, methods=['post'], url_path='prioritize')
    # def prioritize(self, request, pk=None):
    #     try:
    #         plan = self.get_object()

    #         prioritized = PrioritizedThematicCommittee.objects.create(
    #             plan_name=plan.plan_name,
    #             thematic_area=plan.thematic_area,
    #             sub_area=plan.sub_area,
    #             source=plan.source,
    #             expenditure_center=plan.expenditure_center,
    #             budget=plan.budget,
    #             ward_no=plan.ward_no,
    #             status="प्राथमिकरण भएको विषयगत समितिका परियोजना",
    #             priority_no=plan.priority_no,
    #             remarks=plan.remarks,
    #         )

    #         plan.status = "प्राथमिकरण भएको विषयगत समितिका परियोजना"
    #         plan.save()

    #         return Response({"message": "Successfully prioritized."}, status=200)

    #     except PlanEnteredByThematicCommittee.DoesNotExist:
    #         return Response({"error": "Project not found"}, status=404)
    

    @action(detail=True, methods=['post'], url_path='prioritize')
    def prioritize(self, request, pk=None):
        try:
            plan = self.get_object()

            PrioritizedThematicCommittee.objects.create(
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                budget=plan.budget,
                ward_no=plan.ward_no,
                status="प्राथमिकरण भएको विषयगत समितिका परियोजना",
                priority_no=plan.priority_no,
                remarks=plan.remarks,
            )

            # Soft delete the original plan
            plan.status = "प्राथमिकरण भएको विषयगत समितिका परियोजना"
            plan.is_deleted = True
            plan.deleted_at = timezone.now()
            plan.save()

            return Response({"message": "Successfully prioritized and soft-deleted."}, status=200)

        except PlanEnteredByThematicCommittee.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)


