from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail
from projects.serializers.Installment_Payment.payment_related_details import PaymentRelatedDetailSerializer
from projects.models.project import Project
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

# class PaymentRelatedDetailViewSet(viewsets.ModelViewSet):
#     serializer_class = PaymentRelatedDetailSerializer
#     parser_classes = [JSONParser, MultiPartParser, FormParser]
#     def get_queryset(self):
#         project_id = self.kwargs.get("project_id")
#         return PaymentRelatedDetail.objects.filter(project__serial_number=project_id, is_active=True).order_by('-created_at')

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         project_id = self.kwargs.get("project_id")
#         project = get_object_or_404(Project, serial_number=project_id)
#         context['project'] = project
#         return context

#     def perform_create(self, serializer):
#         project = self.get_serializer_context()['project']
#         serializer.save(project=project)

    
class PaymentRelatedDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentRelatedDetailSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]  

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        return PaymentRelatedDetail.objects.filter(project__serial_number=project_id, is_active=True).order_by('-created_at')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        project_id = self.kwargs.get("project_id")
        project = get_object_or_404(Project, serial_number=project_id)
        context['project'] = project
        return context

    def perform_create(self, serializer):
        project = self.get_serializer_context()['project']
        serializer.save(project=project)
        
    
    # def list(self, request, *args, **kwargs):
    #     project   = self.get_serializer_context()["project"]
    #     existing  = self.get_queryset()
    #     existing_titles = set(existing.values_list("title", flat=True))

    #     # All possible titles
    #     all_titles = [choice[0] for choice in PaymentRelatedDetail.TITLE_CHOICES]

    #     # Unsaved “dummy” instance
    #     def _dummy(title):
    #         return PaymentRelatedDetail(
    #             id=None,
    #             project=project,
    #             title=title,
    #             issue_date=None,
    #             amount_paid=None,
    #             payment_percent=None,
    #             physical_progress=None,
    #             uploaded_file=None,
    #             is_active=False,
    #         )

    #     # Combine actual and placeholder records
    #     combined = list(existing) + [
    #         _dummy(t) for t in all_titles if t not in existing_titles
    #     ]

    #     serializer = self.get_serializer(combined, many=True)
    #     return Response(serializer.data)

        
        
        
    
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from datetime import date

from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail
from projects.models.project import Project

def generate_payment_bill_pdf(request, project_id):
    try:
       project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return HttpResponse("Project not found", status=404)

    payment_details = PaymentRelatedDetail.objects.filter(
        project=project, is_active=True
    ).order_by('created_at')

    if not payment_details.exists():
        return HttpResponse("No payment records found", status=404)

    context = {
        "project_name": project.project_name,
        "ward_no": project.ward_no,
        "payments": payment_details,
        "today": date.today().strftime("%Y-%m-%d")
    }

    html_string = render_to_string("Installment_Bill/payment_bill_template.html", context)
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="payment_bill_project_{project_id}.pdf"'
    return response

