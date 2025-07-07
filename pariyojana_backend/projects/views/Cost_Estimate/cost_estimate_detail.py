# projects/views/cost_estimate_detail.py

from rest_framework import viewsets
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
from projects.serializers.Cost_Estimate.cost_estimate_detail import CostEstimateDetailSerializer
from django.shortcuts import render, get_object_or_404
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
from datetime import date
from rest_framework.exceptions import ValidationError
from projects.models.project import Project

class CostEstimateDetailViewSet(viewsets.ModelViewSet):
    queryset = CostEstimateDetail.objects.all()
    serializer_class = CostEstimateDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Support nested URL: /projects/<serial_number>/cost-estimate-details/
        serial_number = self.kwargs.get('serial_number')
        if serial_number:
            queryset = queryset.filter(project__serial_number=serial_number)

        # Support query param: ?project=6
        project_sn = self.request.query_params.get('project')
        if project_sn:
            queryset = queryset.filter(project__serial_number=project_sn)

        return queryset


    def perform_create(self, serializer):
        project_sn = self.request.query_params.get("project")
        if not project_sn:
            raise ValidationError({"detail": "Query param 'project' is required."})
        
        try:
            project = Project.objects.get(serial_number=project_sn)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={project_sn} not found."})

        if CostEstimateDetail.objects.filter(project=project).exists():
            raise ValidationError({"detail": f"Cost estimate already exists for project {project_sn}."})

        serializer.save(project=project)

# POST http://localhost:8000/api/cost-estimate-details/?project=6




    
    
    
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from datetime import date
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail


def generate_bill_pdf(request, project_id):
    try:
        cost_estimate = CostEstimateDetail.objects.get(project_id=project_id)
    except CostEstimateDetail.DoesNotExist:
        return HttpResponse("Cost estimate not found", status=404)

    try:
        consumer_committee = ConsumerCommitteeDetail.objects.get(project_id=project_id)
        committee_name = consumer_committee.consumer_committee_name
    except ConsumerCommitteeDetail.DoesNotExist:
        committee_name = "........."

    context = {
        "project_name": cost_estimate.project.project_name,
        "consumer_committee_name": committee_name,  
        "estimated_cost": cost_estimate.estimated_cost,
        "contingency_percent": cost_estimate.contingency_percent,
        "contingency_amount": cost_estimate.contingency_amount,
        "total_estimated_cost": cost_estimate.total_estimated_cost,
        "allocated_budget": cost_estimate.allocated_budget,
        "today": date.today().strftime("%Y-%m-%d"),
    }

    html_string = render_to_string("Bill_Template/bill_template.html", context)
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_project_{project_id}.pdf"'
    return response



