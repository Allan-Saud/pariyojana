from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from projects.models.consumer_committee import ConsumerCommitteeUpload
from projects.serializers.consumer_committee import ConsumerCommitteeRowSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.http import FileResponse, Http404
from django.conf import settings
import os
from rest_framework.decorators import api_view
from projects.constants import CONSUMER_COMMITTEE_TITLES

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
def download_consumer_committee_letter(request, serial_no):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'consumer_committee_letters', f'{serial_no}.pdf')
    if not os.path.exists(file_path):
        raise Http404("Letter not found.")

    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=f'letter_{serial_no}.pdf')
