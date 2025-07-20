from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from datetime import date
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404
from rest_framework.permissions import AllowAny
from weasyprint import HTML

from projects.models.Project_Aggrement.project_plan_tracker import ProjectPlanTrackerUpload
from projects.serializers.Project_Aggrement.project_plan_tracker import ProjectPlanTrackerRowSerializer
from projects.constants import PROJECT_PLAN_TRACKER_TITLES
from projects.pdfs.plan_aggrement.renderers import render_pdf
from projects.pdfs.plan_aggrement.utils import build_pdf_context


class ProjectPlanTrackerListView(APIView):
    def get(self, request):
        today = date.today()
        uploads = ProjectPlanTrackerUpload.objects.all()
        upload_map = {u.serial_no: u for u in uploads}
        response_data = []

        for item in PROJECT_PLAN_TRACKER_TITLES:
            serial_no = item["serial_no"]
            upload = upload_map.get(serial_no)

            response_data.append({
                "serial_no": serial_no,
                "title": item["title"],
                "date": today,
                "status": "अपलोड गरिएको" if upload else "",
                "file_uploaded_name": upload.file.name.split('/')[-1] if upload else "No file uploaded",
            })

        serializer = ProjectPlanTrackerRowSerializer(response_data, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_project_plan_tracker(request):
    serial_no = request.data.get('serial_no')
    file = request.FILES.get('file')
    remarks = request.data.get('remarks')

    if not serial_no or not file:
        return Response({"detail": "serial_no and file are required."}, status=status.HTTP_400_BAD_REQUEST)

    ProjectPlanTrackerUpload.objects.update_or_create(
        serial_no=serial_no,
        defaults={'file': file, 'remarks': remarks}
    )
    return Response({"detail": "File uploaded successfully."})


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def download_project_plan_tracker_pdf(request, serial_no: int, project_id: int):
#     template_map = {
#         1: "serial_1.html",
#         2: "serial_2.html",
#         3: "serial_3.html",
#         4: "serial_4.html",
#         5: "serial_5.html",
#         6: "serial_6.html",
#     }

#     if not 1 <= serial_no <= 6:
#         raise Http404("Invalid serial_no")

#     context = build_pdf_context(serial_no, project_id)
#     content, filename = render_pdf(template_map[serial_no], context, f"serial_{serial_no}_project_{project_id}.pdf")

#     if content is None:
#         raise Http404("PDF rendering failed.")

#     return HttpResponse(content, content_type='application/pdf', headers={
#         'Content-Disposition': f'attachment; filename="{filename}"',
#     })

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def download_project_plan_tracker_pdf(request, serial_no: int, project_id: int):
#     template_map = {
#         1: "serial_1.html",
#         2: "serial_2.html",
#         3: "serial_3.html",
#         4: "serial_4.html",
#         5: "serial_5.html",
#         6: "serial_6.html",
#     }

#     if serial_no not in template_map:
#         raise Http404("Invalid serial_no")

  
#     context = build_pdf_context(serial_no, project_id)

  
#     upload = ProjectPlanTrackerUpload.objects.filter(serial_no=serial_no).first()
#     if upload:
#         context["file_uploaded_name"] = upload.file.name.split("/")[-1]
#         context["upload_remarks"] = upload.remarks
#         context["uploaded_at"] = upload.uploaded_at.strftime("%Y-%m-%d")
#     else:
#         context["file_uploaded_name"] = "No file uploaded"
#         context["upload_remarks"] = ""
#         context["uploaded_at"] = ""

#     content, filename = render_pdf(
#         template_map[serial_no],
#         context,
#         f"serial_{serial_no}_project_{project_id}.pdf"
#     )

#     if content is None:
#         raise Http404("PDF rendering failed.")

#     return HttpResponse(content, content_type='application/pdf', headers={
#         'Content-Disposition': f'attachment; filename="{filename}"',
#     })


@api_view(['GET'])
@permission_classes([AllowAny])
def download_project_plan_tracker_pdf(request, serial_no: int, project_id: int):
    template_map = {
        1: "plan_aggrement/serial_1.html",
        2: "plan_aggrement/serial_2.html",
        3: "plan_aggrement/serial_3.html",
        4: "plan_aggrement/serial_4.html",
        5: "plan_aggrement/serial_5.html",
        6: "plan_aggrement/serial_6.html",
        7: "plan_aggrement/serial_7.html",
        
    }

    if serial_no not in template_map:
        raise Http404("Invalid serial_no")

    context = build_pdf_context(serial_no, project_id)

    upload = ProjectPlanTrackerUpload.objects.filter(serial_no=serial_no).first()
    if upload:
        context["file_uploaded_name"] = upload.file.name.split("/")[-1]
        context["upload_remarks"] = upload.remarks
        context["uploaded_at"] = upload.uploaded_at.strftime("%Y-%m-%d")
    else:
        context["file_uploaded_name"] = "No file uploaded"
        context["upload_remarks"] = ""
        context["uploaded_at"] = ""

    # Render HTML to string
    html_string = render_to_string(template_map[serial_no], context)

    # Generate PDF bytes using WeasyPrint
    pdf_file = HTML(string=html_string).write_pdf()

    filename = f"serial_{serial_no}_project_{project_id}.pdf"

    if not pdf_file:
        raise Http404("PDF rendering failed.")

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response
    

from projects.models.project import Project
from projects.pdfs.plan_aggrement.utils import build_pdf_context

from django.template.loader import select_template

def preview_project_plan_tracker_template(request, serial_no, project_id):
    context = build_pdf_context(serial_no, project_id)

    templates = [f"plan_aggrement/serial_{serial_no}.html"]
    template = select_template(templates)

    html = template.render(context)
    return HttpResponse(html)



