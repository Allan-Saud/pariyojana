# import os
# from django.conf import settings
# from projects.models.Consumer_Committee.official_detail import OfficialDetail
# from projects.models.project import Project  # or wherever your Project model lives
# from django.conf import settings
# import os

# def build_pdf_context(serial_no, project_id):
#     project = Project.objects.get(serial_number=project_id)
#     officials = OfficialDetail.objects.filter(project=project).order_by('serial_no')

#     # ✅ Absolute file path for logo (required for WeasyPrint to load image)
#     "gov_logo": f'file://{os.path.join(settings.BASE_DIR, "projects/static/images/nepal-govt.png")}'

#     return {
#         "serial_no": serial_no,
#         "project": project,
#         "officials": officials,
#         "project_name": project.project_name,
#         "gov_logo": gov_logo,  # 👉 Inject into context
#     }
import os
from django.conf import settings
from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.models.project import Project

def build_pdf_context(serial_no, project_id):
    project = Project.objects.get(serial_number=project_id)
    officials = OfficialDetail.objects.filter(project=project).order_by('serial_no')

    # ✅ Absolute file path for logo (WeasyPrint requires a file:// URL)
    gov_logo = f'file://{os.path.join(settings.BASE_DIR, "static/images/nepal-govt.png")}'

    return {
        "serial_no": serial_no,
        "project": project,
        "officials": officials,
        "project_name": project.project_name,
        "gov_logo": gov_logo,  # 👉 Injected into context properly
    }
