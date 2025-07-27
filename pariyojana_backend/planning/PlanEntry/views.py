from rest_framework import viewsets, permissions
from .models import PlanEntry
from .serializers import PlanEntrySerializer
from planning.WardOffice.WardLevelProject.models import WardLevelProject
from planning.WardOffice.MunicipalityLevelProject.models import MunicipalityLevelProject  # ✅ import
from planning.ThematicCommittee.PlanEnteredByThematicCommittee.models import PlanEnteredByThematicCommittee
from planning.WardOffice.WardThematicCommitteeProjects.models import WardThematicCommitteeProject
from planning.MunicipalityPrideProject.models import MunicipalityPrideProject
from planning.BudgetProgramcommittee.ProvinciallyTransferredProgram.models import ProvinciallytransferredProgram
from planning.BudgetProgramcommittee.FederalGovernmentProject.models import BudgetProgramFederalGovernmentProgram
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrReadOnly  


class PlanEntryViewSet(viewsets.ModelViewSet):
    queryset = PlanEntry.objects.all()
    serializer_class = PlanEntrySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        plan = serializer.save(created_by=self.request.user)

        if plan.plan_type == "ward_level":
            WardLevelProject.objects.create(
                plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
                status="प्रविष्टी भएको वडा स्तरीय परियोजना",
                remarks=plan.remarks
            )

        elif plan.plan_type == "municipality_level":
            MunicipalityLevelProject.objects.create(
                plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
                status="प्रविष्टी भएको नगर स्तरीय परियोजना",
                remarks=plan.remarks
            )
        elif plan.plan_type == "thematic_committee":
            # Auto-generate priority number (queue-like increment)
            latest = PlanEnteredByThematicCommittee.objects.order_by("-priority_no").first()
            next_priority = (latest.priority_no + 1) if latest and latest.priority_no else 1

            PlanEnteredByThematicCommittee.objects.create(
                 plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
                status="विषयगत समितिमा प्रविष्टी भएको",
                priority_no=next_priority,
                remarks=plan.remarks
            )
            
        elif plan.plan_type == "ward_requested_thematic":
            latest = WardThematicCommitteeProject.objects.order_by("-priority_no").first()
            next_priority = (latest.priority_no + 1) if latest and latest.priority_no else 1

            WardThematicCommitteeProject.objects.create(
                 plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
                status="वडाले माग गर्ने विषयगत समितिका परियोजना",
                priority_no=next_priority,
                remarks=plan.remarks
            )
            
        elif plan.plan_type == "pride_project":
            MunicipalityPrideProject.objects.create(
                plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
                status="प्राइड परियोजना अन्तर्गत प्रविष्टी भएको",  
                remarks=plan.remarks
            )
        
        elif plan.plan_type == "provincial":
         ProvinciallytransferredProgram.objects.create(
             plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
            status="प्रदेश परियोजना अन्तर्गत प्रविष्टी भएको",
            remarks=plan.remarks
        )
        
        elif plan.plan_type == "federal":
            BudgetProgramFederalGovernmentProgram.objects.create(
                 plan_entry=plan,
                plan_name=plan.plan_name,
                thematic_area=plan.thematic_area,
                sub_area=plan.sub_area,
                source=plan.source,
                expenditure_center=plan.expenditure_center,
                expenditure_title=plan.expenditure_title,
                budget=plan.proposed_amount,
                ward_no=plan.ward_no,
                gps_coordinate=plan.gps_coordinate,
                expected_result=plan.expected_result,
                unit=plan.unit,
                location=plan.location,
                project_level=plan.project_level,
                feasibility_study=plan.feasibility_study,
                feasibility_file=plan.feasibility_file,
                detailed_study=plan.detailed_study,
                detailed_file=plan.detailed_file,
                environmental_study=plan.environmental_study,
                environmental_file=plan.environmental_file,
                status="संघीय सरकार अन्तर्गतको परियोजना",
                remarks=plan.remarks
            )


