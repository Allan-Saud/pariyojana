from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from projects.models.Consumer_Committee.consumer_committee import ConsumerCommitteeUpload
from projects.serializers.Consumer_Committee.consumer_committee import ConsumerCommitteeRowSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, Http404
from projects.constants import CONSUMER_COMMITTEE_TITLES
from rest_framework.permissions import AllowAny
from weasyprint import HTML
from django.template.loader import render_to_string
import nepali_datetime as ndt
from django.templatetags.static import static
from django.conf import settings
import os
from django.template.loader import get_template
from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
from projects.pdfs.consumer_committee.renderers import render_pdf
from projects.models.project import Project
from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember



def build_pdf_context(serial_no, project_serial_number):
    context = {}

    try:
        project = Project.objects.get(serial_number=project_serial_number)

        # Try to fetch committee details if available
        committee = ConsumerCommitteeDetail.objects.filter(project=project, is_active=True).first()
        image_relative_path = 'images/nepal-govt.png'
        image_absolute_path = os.path.join(settings.BASE_DIR, 'static', image_relative_path)
        image_uri = f'file://{image_absolute_path}'
        
        context.update({
            "project_name": project.project_name,
            "fiscal_year": project.fiscal_year if project.fiscal_year else "",
            "location": project.location or "-",
            "total_cost": f"{project.budget} रू",  # fallback using budget
            "budget_title": project.source.name if project.source else "-",
            # "agreement_date": project.created_at.date() if project.created_at else "-",
            "execution_date": "-",
            # "completion_date": project.updated_at.date() if project.updated_at else "-",
            "expense_date": "-",
            "payment_date": "-",
            "chairman_name": committee.representative_name if committee else "-",
            "contact_number": committee.contact_no if committee else "-",
            "agreement_date": ndt.date.from_datetime_date(project.created_at.date()).strftime("%K-%n-%D गते") if project.created_at else "-",
            "completion_date": ndt.date.from_datetime_date(project.updated_at.date()).strftime("%K-%n-%D गते") if project.updated_at else "-",
            "gov_logo": image_uri,

        })

        # Extra for serial 4
        if serial_no == 4:
            context["consumer_committee_details"] = committee
            
            
        if serial_no == 5:
            # officials
            officials = OfficialDetail.objects.filter(project=project).order_by("serial_no")
            official_by_post = {
                "chairman": "",
                "secretary": "",
                "treasurer": "",
                "members": [],
            }

            for o in officials:
                if o.post == "अध्यक्ष":
                    official_by_post["chairman"] = o.full_name
                elif o.post == "सचिव":
                    official_by_post["secretary"] = o.full_name
                elif o.post == "कोषाध्यक्ष":
                    official_by_post["treasurer"] = o.full_name
                elif o.post == "सदस्य":
                    official_by_post["members"].append(o.full_name)



            # monitoring committee
            monitors = MonitoringFacilitationCommitteeMember.objects.filter(project=project).order_by("serial_no")
            monitoring_by_post = {
                "coordinator": "",
                "member_secretary": "",
                "members": [],
            }

            for m in monitors:
                if m.post == "संयोजक":
                    monitoring_by_post["coordinator"] = m.full_name
                elif m.post == "सदस्य सचिव":
                    monitoring_by_post["member_secretary"] = m.full_name
                elif m.post == "सदस्य":
                    monitoring_by_post["members"].append(m.full_name)



            context["official_by_post"] = official_by_post
            context["monitoring_by_post"] = monitoring_by_post
            context["range_2_46"] = range(2, 46) 
            
        
        if serial_no == 6:
            officials_qs = OfficialDetail.objects.filter(project=project).order_by('serial_no')
            print(f"Officials count for project {project.serial_number}: {officials_qs.count()}")
            context["officials"] = officials_qs

            
        



        return context

    except Project.DoesNotExist:
        raise Http404("Project not found.")

CONSUMER_COMMITTEE_TITLES = [
    {"serial_no": 1, "title": "योजना संचालन पुस्तिका विवरण पृष्ट"},
    {"serial_no": 2, "title": "उपभोक्ता समिति गठन विधि एवं प्रकृया"},
    {"serial_no": 3, "title": "उपभोत्ता समिति गठन गर्ने सम्बन्धी सुचना"},
    {"serial_no": 4, "title": "उपभोत्ता समितिको काम कर्तव्य र अधिकारको विवरण"},
    {"serial_no": 5, "title": "आम भेलाको माईनियुट (उपभोक्ता समिति गठन गर्दा छलफल तथा भेलाका विषयबस्तुहरु)"},
    {"serial_no": 6, "title": "उपभोक्ता समिति गठन गरि पठाइएको बारे (प्रतीनिधीले वडा कार्यालयलाई पेस गर्ने निवेदन )"},
    {"serial_no": 7, "title": "उपभोत्ता समितिले स्वीकृत गरेको अनुमान स्वीकृति टिप्पणी"}
]

class ConsumerCommitteeListView(APIView):
    def get(self, request):
        today = date.today()

        uploads = ConsumerCommitteeUpload.objects.all()
        upload_map = {u.serial_no: u for u in uploads}

        response_data = []

        for item in CONSUMER_COMMITTEE_TITLES:
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

        serializer = ConsumerCommitteeRowSerializer(response_data, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def consumer_committee_upload(request, serial_number):
    print("In consumer_committee_upload view, serial_number:", serial_number)
    from projects.models.project import Project

    try:
        project = Project.objects.get(serial_number=serial_number)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

    serial_no = request.data.get('serial_no')
    file = request.FILES.get('file')
    remarks = request.data.get('remarks')

    if not serial_no or not file:
        return Response({"detail": "serial_no and file are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Optionally store the project as a ForeignKey in the model
    obj, created = ConsumerCommitteeUpload.objects.update_or_create(
        serial_no=serial_no,
        defaults={
            'file': file,
            'remarks': remarks,
            # If your model has `project = models.ForeignKey(Project)`:
            # 'project': project
        }
    )

    return Response({"detail": "File uploaded successfully."})


@api_view(['GET'])
@permission_classes([AllowAny])
def download_consumer_committee_pdf(request, serial_no: int, project_id: int):
    if not 1 <= serial_no <= 6:
        raise Http404("Template not available.")

    template_map = {
        1: "serial_1.html",
        2: "serial_2.html",
        3: "serial_3.html",
        4: "serial_4.html",
        5: "serial_5.html",
        6: "serial_6.html",
        7: "serial_7.html"
    }

    # Build the context for the template (assuming you have this function)
    context = build_pdf_context(serial_no, project_id)

    # Render the HTML template to a string
    html_string = render_to_string(template_map[serial_no], context)

    # Use WeasyPrint to convert HTML to PDF bytes
    pdf_file = HTML(string=html_string).write_pdf()

    filename = f"serial_{serial_no}_project_{project_id}.pdf"

    if not pdf_file:
        raise Http404("PDF rendering failed.")

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response


def preview_template(request, serial_no=1, project_id=4):
    context = build_pdf_context(serial_no, project_id)
    html = get_template(f"serial_{serial_no}.html").render(context)
    return HttpResponse(html)
