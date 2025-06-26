# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.shortcuts import get_object_or_404
# from projects.models.project import Project
# from projects.models.program_detail import ProgramDetail, BeneficiaryDetail
# from projects.models.budget_estimate import BudgetEstimate
# from projects.models.agreement import Agreement
# from projects.models.consumer_committee import ConsumerCommittee
# from projects.models.initiation_process import InitiationProcess
# from projects.models.operation_location import OperationLocation
# from projects.models.payment_installment import PaymentInstallment
# from projects.serializers.program_detail import ProgramDetailSerializer

# class ProgramDetailViewSet(viewsets.ViewSet):

#     def retrieve(self, request, pk=None):
#         project = get_object_or_404(Project, pk=pk)

#         # ProgramDetail info (create or retrieve)
#         program_detail, _ = ProgramDetail.objects.get_or_create(project=project)

#         # Fill data from Project model (snapshots)
#         program_detail.project_name = project.project_name
#         program_detail.ward_no = project.ward_no
#         program_detail.fiscal_year = project.fiscal_year
#         program_detail.area = project.area
#         program_detail.sub_area = project.sub_area
#         program_detail.expenditure_center = project.expenditure_center
#         program_detail.source = project.source

#         # Fill data from subcomponents (if exist)
#         program_detail.location = getattr(OperationLocation.objects.filter(project=project).first(), 'location', '')
#         program_detail.project_level = getattr(InitiationProcess.objects.filter(project=project).first(), 'project_level', '')
#         program_detail.allocated_budget = project.budget
#         program_detail.expected_output = getattr(InitiationProcess.objects.filter(project=project).first(), 'output_count', 0)
#         program_detail.gps_coordinate = getattr(OperationLocation.objects.filter(project=project).first(), 'gps_coordinate', '')
#         program_detail.status = project.status

#         program_detail.start_date = getattr(InitiationProcess.objects.filter(project=project).first(), 'start_date', None)
#         program_detail.agreement_date = getattr(Agreement.objects.filter(project=project).first(), 'agreement_date', None)
#         program_detail.completion_date = getattr(InitiationProcess.objects.filter(project=project).first(), 'completion_date', None)
#         program_detail.economic_progress = getattr(PaymentInstallment.objects.filter(project=project).first(), 'economic_progress', 0)
#         program_detail.physical_progress = getattr(ConsumerCommittee.objects.filter(project=project).first(), 'physical_progress', 0)
#         program_detail.estimated_cost = getattr(BudgetEstimate.objects.filter(project=project).first(), 'estimated_cost', 0)
#         program_detail.contingency_amount = getattr(BudgetEstimate.objects.filter(project=project).first(), 'contingency_amount', 0)
#         program_detail.agreement_amount = getattr(Agreement.objects.filter(project=project).first(), 'agreement_amount', 0)
#         program_detail.consumer_contribution = getattr(ConsumerCommittee.objects.filter(project=project).first(), 'contribution_amount', 0)

#         program_detail.save()
#         serializer = ProgramDetailSerializer(program_detail)
#         return Response(serializer.data)

#     @action(detail=True, methods=['post'])
#     def set_beneficiaries(self, request, pk=None):
#         program_detail = get_object_or_404(ProgramDetail, project_id=pk)
#         BeneficiaryDetail.objects.filter(program_detail=program_detail).delete()

#         input_data = request.data
#         summary = [
#             {"title": "जम्मा परिवार", "female": 0, "male": 0, "others": 0, "total": input_data.get("total_household", 0)},
#             {"title": "जम्मा जनसंख्या", "female": input_data.get("female_population", 0), "male": input_data.get("male_population", 0), "others": input_data.get("other_population", 0)},
#             {"title": "आदिवासी जनजातिको परिवार संख्या", "female": 0, "male": 0, "others": 0, "total": input_data.get("tribal_household", 0)},
#             {"title": "दलित वर्गको परिवार संख्या", "female": 0, "male": 0, "others": 0, "total": input_data.get("dalit_household", 0)},
#             {"title": "बालबालिकाको जनसंख्या", "female": input_data.get("child_female", 0), "male": input_data.get("child_male", 0), "others": input_data.get("child_other", 0)},
#             {"title": "अन्य वर्गको परिवार संख्या", "female": input_data.get("other_female", 0), "male": input_data.get("other_male", 0), "others": input_data.get("other_other", 0)},
#         ]

#         for data in summary:
#             BeneficiaryDetail.objects.create(
#                 program_detail=program_detail,
#                 title=data["title"],
#                 female=data.get("female", 0),
#                 male=data.get("male", 0),
#                 others=data.get("others", 0),
#             )

#         return Response({"message": "Beneficiary data saved."}, status=status.HTTP_201_CREATED)
