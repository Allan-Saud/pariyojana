from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from projects.models.project import Project
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails

class ProjectRelatedDataView(APIView):

    def get(self, request, serial_number):
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            return Response({"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

        # Fetch related cost estimate details
        try:
            cost_estimate = CostEstimateDetail.objects.get(project=project)
        except CostEstimateDetail.DoesNotExist:
            cost_estimate = None

        # Fetch related agreement details
        try:
            agreement = ProjectAgreementDetails.objects.get(project=project)
        except ProjectAgreementDetails.DoesNotExist:
            agreement = None

        data = {
            # "project_id": project.serial_number,
            "serial_number": project.serial_number,
            "estimated_cost": cost_estimate.estimated_cost if cost_estimate else None,
            "contingency_amount": cost_estimate.contingency_amount if cost_estimate else None,
            "agreement_date": agreement.agreement_date if agreement else None,
            "start_date": agreement.work_order_date if agreement else None,
            "completion_date": agreement.completion_date if agreement else None,
            "agreement_amount": agreement.agreement_amount if agreement else None,
            "public_participation_amount": agreement.public_participation_amount if agreement else None,
        }

        return Response(data)
