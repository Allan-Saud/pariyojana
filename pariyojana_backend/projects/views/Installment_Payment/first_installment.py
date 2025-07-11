# projects/views/Installment_Payment/first_installment.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404
from datetime import date
import os
from django.http import FileResponse
from django.conf import settings
from projects.models.Installment_Payment.first_installment import FirstInstallmentUpload
from projects.serializers.Installment_Payment.first_installment import FirstInstallmentRowSerializer
from projects.constants import FIRST_INSTALLMENT_TITLES
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from projects.models.project import Project
from rest_framework import viewsets

# class FirstInstallmentListView(APIView):
class FirstInstallmentListView(APIView):
    def get(self, request, project_id):
        today = date.today()

        uploads = FirstInstallmentUpload.objects.filter(project_id=project_id)
        upload_map = {u.serial_no: u for u in uploads}

        response_data = []

        for item in FIRST_INSTALLMENT_TITLES:
            serial_no = item["serial_no"]
            upload = upload_map.get(serial_no)

            if upload:
                status_text = "अपलोड गरिएको"
                file_uploaded_name = upload.file.name.split('/')[-1] if upload.file else ""
                remarks = getattr(upload, 'remarks', None)
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

        serializer = FirstInstallmentRowSerializer(response_data, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_first_installment_file(request, project_id):
    serial_no = request.data.get('serial_no')
    file = request.FILES.get('file')
    remarks = request.data.get('remarks')

    if not serial_no:
        return Response({"detail": "serial_no is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        project = Project.objects.get(serial_number=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

    defaults = {'remarks': remarks}
    if file:
        defaults['file'] = file

    obj, created = FirstInstallmentUpload.objects.update_or_create(
        project=project,
        serial_no=serial_no,
        defaults=defaults
    )

    return Response({"detail": "File uploaded successfully."})


@api_view(['GET'])
@permission_classes([AllowAny])
def download_first_installment_file(request, project_id, serial_no):
    try:
        upload = FirstInstallmentUpload.objects.get(project_id=project_id, serial_no=serial_no)
        file_path = upload.file.path

        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        else:
            raise Http404("File not found.")
    except FirstInstallmentUpload.DoesNotExist:
        raise Http404("No file uploaded for this serial number and project.")




# Method	URL	Action
# GET	/first-installment/	            List all uploads
# POST	/first-installment/	             Upload file (via ViewSet)
# GET	/first-installment/<id>/	    Get by ID
# PATCH	/first-installment/<id>/	       Update by ID
# POST	/first-installment/upload/	      Upload (custom view, same logic)  
    
    
    
# projects/views/Installment_Payment/first_installment.py

from projects.pdfs.First_Installment.utils import build_pdf_context
from projects.pdfs.First_Installment.renderers import render_pdf 
from django.template.loader import get_template

@api_view(['GET'])
@permission_classes([AllowAny])
def download_first_installment_pdf(request, serial_no: int, project_id: int):
    template_map = {
        1: "serial_1.html",
        2: "serial_2.html",
        3: "serial_3.html",
    }

    if serial_no not in template_map:
        raise Http404("Template not available.")

    context = build_pdf_context(serial_no, project_id)
    content, filename = render_pdf(f"First_Installment/{template_map[serial_no]}", context, f"first_installment_{serial_no}_project_{project_id}.pdf")

    if content is None:
        raise Http404("PDF rendering failed.")

    return HttpResponse(content, content_type='application/pdf', headers={
        'Content-Disposition': f'attachment; filename="{filename}"',
    })

from django.template.loader import select_template
from django.template.exceptions import TemplateDoesNotExist
@api_view(['GET'])
@permission_classes([AllowAny])
def preview_first_installment_template(request, serial_no: int, project_id: int):
    context = build_pdf_context(serial_no, project_id)

    templates = [
        f"First_Installment/serial_{serial_no}.html",
        f"serial_{serial_no}.html",  # fallback
    ]

    try:
        template = select_template(templates)
    except TemplateDoesNotExist:
        raise Http404("Template not found.")

    html = template.render(context)
    return HttpResponse(html)

