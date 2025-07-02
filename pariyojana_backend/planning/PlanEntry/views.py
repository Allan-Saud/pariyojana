from rest_framework import viewsets, permissions
from .models import PlanEntry
from .serializers import PlanEntrySerializer
from planning.WardOffice.WardLevelProject.models import WardLevelProject

class PlanEntryViewSet(viewsets.ModelViewSet):
    queryset = PlanEntry.objects.all()
    serializer_class = PlanEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        plan = serializer.save(created_by=self.request.user)

        # Auto-create WardLevelProject entry
        WardLevelProject.objects.create(
            plan_name=plan.plan_name,
            thematic_area=plan.thematic_area,
            sub_area=plan.sub_area,
            source=plan.source,
            expenditure_center=plan.expenditure_center,
            budget=plan.proposed_amount,
            ward_no=plan.ward_no,
            status="प्रविष्टी भएको वडा स्तरीय परियोजना"
        )
