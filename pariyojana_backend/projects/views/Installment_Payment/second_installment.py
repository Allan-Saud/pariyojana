from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from projects.models.Installment_Payment.second_installment import SecondInstallment
from projects.serializers.Installment_Payment.second_installment import SecondInstallmentRowSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from django.http import HttpResponse, Http404
from projects.constants import SECOND_INSTALLMENT_TITLES
from django.template.loader import get_template
from projects.pdfs.Second_Installment.renderers import render_pdf
from projects.models.project import Project
from projects.pdfs.Second_Installment.utils import build_pdf_context

class SecondInstallmentListView(APIView):
    def get(self, request, project_id):
        today = date.today()

        uploads = SecondInstallment.objects.filter(project_id=project_id)
        upload_map = {u.serial_no: u for u in uploads}

        response_data = []

        for item in SECOND_INSTALLMENT_TITLES:
            serial_no = item["serial_no"]
            upload = upload_map.get(serial_no)

            if upload:
                status_text = "अपलोड गरिएको"
                file_uploaded_name = upload.file.name.split('/')[-1] if upload.file else ""
                remarks = upload.remarks
            else:
                status_text = ""
                file_uploaded_name = ""
                remarks = None

            response_data.append({
                "serial_no": serial_no,
                "title": item["title"],
                "date": today,
                "status": status_text,
                "file_uploaded_name": file_uploaded_name,
                "remarks": remarks,
            })

        serializer = SecondInstallmentRowSerializer(response_data, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def second_installment_upload(request, project_id):
    serial_no = request.data.get('serial_no')
    file = request.FILES.get('file')
    remarks = request.data.get('remarks')

    if not serial_no:
        return Response({"detail": "serial_no is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

    obj, created = SecondInstallment.objects.update_or_create(
        project=project,
        serial_no=serial_no,
        defaults={'file': file, 'remarks': remarks} if file else {'remarks': remarks}
    )
    return Response({"detail": "File uploaded successfully."})

@api_view(['GET'])
def download_second_installment_pdf(request, serial_no: int, project_id: int):
    if not 1 <= serial_no <= 9:
        raise Http404("Template not available.")

    template_map = {
        1: "serial_1.html",
        2: "serial_2.html",
        3: "serial_3.html",
        4: "serial_4.html",
        5: "serial_5.html",
        6: "serial_6.html",
        7: "serial_7.html",
        8: "serial_8.html",
        9: "serial_9.html",
    }

    context = build_pdf_context(serial_no, project_id)
    content, filename = render_pdf(template_map[serial_no], context, f"second_installment_{serial_no}_project_{project_id}.pdf")

    if content is None:
        raise Http404("PDF rendering failed.")

    return HttpResponse(content, content_type='application/pdf', headers={
        'Content-Disposition': f'attachment; filename="{filename}"',
    })

def preview_template(request, serial_no=1, project_id=1):
    context = build_pdf_context(serial_no, project_id)
    html = get_template(f"second_installment/serial_{serial_no}.html").render(context)
    return HttpResponse(html)