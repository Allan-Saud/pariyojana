from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail
from projects.serializers.Installment_Payment.payment_related_details import PaymentRelatedDetailSerializer
from projects.models.project import Project
class PaymentRelatedDetailViewSet(viewsets.ModelViewSet):
    queryset = PaymentRelatedDetail.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = PaymentRelatedDetailSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
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

