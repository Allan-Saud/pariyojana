from rest_framework import viewsets, permissions
from .models import PlanEntry
from .serializers import PlanEntrySerializer
from planning.WardOffice.WardLevelProject.models import WardLevelProject
from planning.WardOffice.MunicipalityLevelProject.models import MunicipalityLevelProject  # ✅ import
from planning.ThematicCommittee.PlanEnteredByThematicCommittee.models import PlanEnteredByThematicCommittee
from planning.WardOffice.WardThematicCommitteeProjects.models import WardThematicCommitteeProject

class PlanEntryViewSet(viewsets.ModelViewSet):
    queryset = PlanEntry.objects.all()
    serializer_class = PlanEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        plan = serializer.save(created_by=self.request.user)

        if plan.plan_type == "ward_level":
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

        elif plan.plan_type == "municipality_level":
            MunicipalityLevelProject.objects.create(
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                status="प्रविष्टी भएको नगर स्तरीय परियोजना"
            )
        elif plan.plan_type == "thematic_committee":
            # Auto-generate priority number (queue-like increment)
            latest = PlanEnteredByThematicCommittee.objects.order_by("-priority_no").first()
            next_priority = (latest.priority_no + 1) if latest and latest.priority_no else 1

            PlanEnteredByThematicCommittee.objects.create(
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                status="विषयगत समितिमा प्रविष्टी भएको",
                priority_no=next_priority,
                remarks=plan.remarks
            )
            
        elif plan.plan_type == "ward_request_thematic":
            latest = WardThematicCommitteeProject.objects.order_by("-priority_no").first()
            next_priority = (latest.priority_no + 1) if latest and latest.priority_no else 1

            WardThematicCommitteeProject.objects.create(
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                status="वडाले माग गर्ने विषयगत समितिका परियोजना",
                priority_no=next_priority,
                remarks=plan.remarks
            )
