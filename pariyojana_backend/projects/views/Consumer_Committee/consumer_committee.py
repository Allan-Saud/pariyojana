from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from projects.models.Consumer_Committee.consumer_committee import ConsumerCommitteeUpload
from projects.serializers.Consumer_Committee.consumer_committee import ConsumerCommitteeRowSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from django.http import FileResponse, Http404
from django.conf import settings
import os
from projects.constants import CONSUMER_COMMITTEE_TITLES
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# from projects.pdfs.consumer_committee.utils import build_pdf_context
# from projects.pdfs.consumer_committee.renderers import render_pdf

CONSUMER_COMMITTEE_TITLES = [
    {"serial_no": 1, "title": "योजना संचालन पुस्तिका विवरण पृष्ट"},
    {"serial_no": 2, "title": "उपभोक्ता समिति गठन विधि एवं प्रकृया"},
    {"serial_no": 3, "title": "उपभोत्ता समिति गठन गर्ने सम्बन्धी सुचना"},
    {"serial_no": 4, "title": "उपभोत्ता समितिको काम कर्तव्य र अधिकारको विवरण"},
    {"serial_no": 5, "title": "आम भेलाको माईनियुट (उपभोक्ता समिति गठन गर्दा छलफल तथा भेलाका विषयबस्तुहरु)"},
    {"serial_no": 6, "title": "उपभोक्ता समिति गठन गरि पठाइएको बारे (प्रतीनिधीले वडा कार्यालयलाई पेस गर्ने निवेदन )"},
]

class ConsumerCommitteeListView(APIView):

    def get(self, request):
        today = date.today()  # For Nepali date, you need a conversion lib

        # Get all uploads indexed by serial_no
        uploads = ConsumerCommitteeUpload.objects.all()
        upload_map = {u.serial_no: u for u in uploads}

        response_data = []

        for item in CONSUMER_COMMITTEE_TITLES:
            serial_no = item["serial_no"]
            upload = upload_map.get(serial_no)
            if upload:
                status = "अपलोड गरिएको"
                file_uploaded_name = upload.file.name.split('/')[-1]
            else:
                status = ""
                file_uploaded_name = "No file uploaded"

            response_data.append({
                "serial_no": serial_no,
                "title": item["title"],
                "date": today,
                "status": status,
                "file_uploaded_name": file_uploaded_name,
            })

        serializer = ConsumerCommitteeRowSerializer(response_data, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def consumer_committee_upload(request):
    serial_no = request.data.get('serial_no')
    file = request.FILES.get('file')
    remarks = request.data.get('remarks')

    if not serial_no or not file:
        return Response({"detail": "serial_no and file are required."}, status=status.HTTP_400_BAD_REQUEST)

    obj, created = ConsumerCommitteeUpload.objects.update_or_create(
        serial_no=serial_no,
        defaults={'file': file, 'remarks': remarks}
    )
    return Response({"detail": "File uploaded successfully."})



@api_view(['GET'])
@permission_classes([AllowAny])
def download_consumer_committee_pdf(request, serial_no: int, project_id: int):
    if not 1 <= serial_no <= 6:
        raise Http404("Template not available.")

    # template_map = {
    #     1: "projects/pdfs/consumer_committee/templates/serial_1.html",
    #     2: "projects/pdfs/consumer_committee/templates/serial_2.html",
    #     3: "projects/pdfs/consumer_committee/templates/serial_3.html",
    #     4: "projects/pdfs/consumer_committee/templates/serial_4.html",
    #     5: "projects/pdfs/consumer_committee/templates/serial_5.html",
    #     6: "projects/pdfs/consumer_committee/templates/serial_6.html",
    # }
    template_map = {
        1: "serial_1.html",
        2: "serial_2.html",
        3: "serial_3.html",
        4: "serial_4.html",
        5: "serial_5.html",
        6: "serial_6.html",
    }


    from projects.pdfs.consumer_committee.utils import build_pdf_context
    from projects.pdfs.consumer_committee.renderers import render_pdf

    context = build_pdf_context(serial_no, project_id)
    content, filename = render_pdf(template_map[serial_no], context, f"serial_{serial_no}_project_{project_id}.pdf")

    if content is None:
        raise Http404("PDF rendering failed.")

    return HttpResponse(content, content_type='application/pdf', headers={
        'Content-Disposition': f'attachment; filename="{filename}"',
    })


from projects.pdfs.consumer_committee.utils import build_pdf_context

def preview_template(request):
    from django.template.loader import get_template
    context = build_pdf_context(1, 4)
    # html = get_template("serial_1.html").render(context)
    html = get_template("serial_3.html").render(context)
    return HttpResponse(html)  # View raw HTML in browser

