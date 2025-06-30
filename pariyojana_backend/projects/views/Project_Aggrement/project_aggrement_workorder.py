from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from projects.models.Project_Aggrement.project_aggrement_workorder import ProjectAgreementWorkorderUpload
from projects.serializers.Project_Aggrement.project_aggrement_workorder import ProjectAgreementWorkorderRowSerializer
from projects.constants import PROJECT_AGREEMENT_WORKORDER_TITLES
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from projects.pdfs.project_aggrement_workorder.renderers import render_pdf
from projects.pdfs.project_aggrement_workorder.utils import build_pdf_context
from django.http import HttpResponse, Http404

class ProjectAgreementWorkorderListView(APIView):
    def get(self, request):
        today = date.today()

        uploads = ProjectAgreementWorkorderUpload.objects.all()
        upload_map = {u.serial_no: u for u in uploads}

        response_data = []

        for item in PROJECT_AGREEMENT_WORKORDER_TITLES:
            serial_no = item["serial_no"]
            upload = upload_map.get(serial_no)
            if upload:
                status_text = "अपलोड गरिएको"
                file_uploaded_name = upload.file.name.split('/')[-1]
            else:
                status_text = ""
                file_uploaded_name = "No file uploaded"

            response_data.append({
                "serial_no": serial_no,
                "title": item["title"],
                "date": today,
                "status": status_text,
                "file_uploaded_name": file_uploaded_name,
            })

        serializer = ProjectAgreementWorkorderRowSerializer(response_data, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def project_agreement_workorder_upload(request):
    serial_no = request.data.get('serial_no')
    file = request.FILES.get('file')
    remarks = request.data.get('remarks')

    if not serial_no or not file:
        return Response({"detail": "serial_no and file are required."}, status=status.HTTP_400_BAD_REQUEST)

    obj, created = ProjectAgreementWorkorderUpload.objects.update_or_create(
        serial_no=serial_no,
        defaults={'file': file, 'remarks': remarks}
    )
    return Response({"detail": "File uploaded successfully."})




@api_view(['GET'])
def download_project_agreement_workorder_pdf(request, serial_no: int, project_id: int):
    if serial_no not in [1, 2, 3, 4]:
        raise Http404("Template not available.")

    template_map = {
        1: "serial_1.html",
        2: "serial_2.html",
        3: "serial_3.html",
        4: "serial_4.html",
    }

    context = build_pdf_context(serial_no, project_id)
    content, filename = render_pdf(template_map[serial_no], context, f"serial_{serial_no}_project_{project_id}.pdf")

    if content is None:
        raise Http404("PDF rendering failed.")

    return HttpResponse(content, content_type='application/pdf', headers={
        'Content-Disposition': f'attachment; filename="{filename}"',
    })




from django.template.loader import select_template

def preview_project_aggrement_workorder_template(request, serial_no, project_id):
    context = build_pdf_context(serial_no, project_id)
    templates = [
        f"project_aggrement_workorder/serial_{serial_no}.html",
        f"serial_{serial_no}.html",
    ]
    template = select_template(templates)

    html = template.render(context)
    return HttpResponse(html)

