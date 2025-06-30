from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, parsers
from projects.models.Installment_Payment.first_installment import FirstInstallmentDocument
from projects.serializers.Installment_Payment.first_installment import FirstInstallmentDocumentSerializer

class FirstInstallmentDocumentView(APIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get(self, request):
        # Make sure all 3 serials exist in DB to show
        for i in range(1,4):
            FirstInstallmentDocument.objects.get_or_create(serial_number=i)

        docs = FirstInstallmentDocument.objects.all().order_by('serial_number')
        serializer = FirstInstallmentDocumentSerializer(docs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serial_number = request.data.get('serial_number')
        if not serial_number:
            return Response({"error": "serial_number is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serial_number = int(serial_number)
            doc = FirstInstallmentDocument.objects.get(serial_number=serial_number)
        except (ValueError, FirstInstallmentDocument.DoesNotExist):
            return Response({"error": "Invalid serial_number"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FirstInstallmentDocumentSerializer(doc, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit  # Or use your existing PDF rendering utility

class FirstInstallmentPDFView(APIView):
    def get(self, request, serial_number):
        try:
            serial_number = int(serial_number)
            doc = FirstInstallmentDocument.objects.get(serial_number=serial_number)
        except (ValueError, FirstInstallmentDocument.DoesNotExist):
            return Response({"error": "Invalid serial_number"}, status=status.HTTP_404_NOT_FOUND)

        html = render_to_string(f'pdfs/consumer_committee/serial_{serial_number}.html', {'doc': doc})
        pdf = pdfkit.from_string(html, False)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="installment_{serial_number}.pdf"'
        return response
