from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from datetime import date
from rest_framework.decorators import api_view
from projects.serializers.Documents.other_document import OtherDocumentSerializer
from projects.pdfs.other_documents.utils import build_pdf_context
from projects.pdfs.other_documents.renderers import render_pdf
from projects.models.project import Project
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from weasyprint import HTML

DOCUMENT_TITLES = [
    {"serial_no": 1, "title": "योजना कार्यन्वयन चेक लिष्ट"},
    {"serial_no": 2, "title": "खर्च तेरिज"},
    {"serial_no": 3, "title": "डोर हाजिर विवरण"},
]

class OtherDocumentListView(APIView):
    def get(self, request, project_id):
        today = date.today()
        response_data = []

        for item in DOCUMENT_TITLES:
            response_data.append({
                "serial_no": item["serial_no"],
                "title": item["title"],
                "date": today,
                "status": "",  # Blank
            })

        return Response(response_data)
    
    def post(self, request, project_id):
        # get the primary key field of Project
        pk_field = Project._meta.pk.name
        
        try:
            project = Project.objects.get(**{pk_field: project_id})
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
        
        data = request.data.copy()
        data['project'] = project.pk  # or project_id
        
        serializer = OtherDocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(project=project)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# @api_view(["GET"])
# def download_other_document_pdf(request, serial_no, project_id):
#     if serial_no not in [1, 2, 3]:
#         raise Http404("Template not available")

#     template_map = {
#         1: "other_documents/serial_1.html",
#         2: "other_documents/serial_2.html",
#         3: "other_documents/serial_3.html",
#     }

#     context = build_pdf_context(serial_no, project_id)
#     content, filename = render_pdf(template_map[serial_no], context, f"serial_{serial_no}_project_{project_id}.pdf")

#     if content is None:
#         raise Http404("PDF rendering failed.")

#     return HttpResponse(content, content_type="application/pdf", headers={
#         'Content-Disposition': f'attachment; filename="{filename}"'
#     })



@api_view(["GET"])
def download_other_document_pdf(request, serial_no, project_id):
    if serial_no not in [1, 2, 3]:
        raise Http404("Template not available")

    template_map = {
        1: "other_documents/serial_1.html",
        2: "other_documents/serial_2.html",
        3: "other_documents/serial_3.html",
    }

    context = build_pdf_context(serial_no, project_id)

    html_string = render_to_string(template_map[serial_no], context)
    pdf_file = HTML(string=html_string).write_pdf()

    filename = f"serial_{serial_no}_project_{project_id}.pdf"

    if not pdf_file:
        raise Http404("PDF rendering failed.")

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

    
    
from django.template.loader import select_template

def preview_other_document_template(request, serial_no, project_id):
    context = build_pdf_context(serial_no, project_id)
    templates = [
        f"other_documents/serial_{serial_no}.html",
        f"serial_{serial_no}.html",
    ]
    template = select_template(templates)

    html = template.render(context)
    return HttpResponse(html)
