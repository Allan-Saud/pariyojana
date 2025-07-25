import os
from django.conf import settings
from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.models.project import Project  # or wherever your Project model lives

def build_pdf_context(serial_no, project_id):
    project = Project.objects.get(serial_number=project_id)
    officials = OfficialDetail.objects.filter(project=project).order_by('serial_no')

    # ✅ Absolute file path for logo (required for WeasyPrint to load image)
    image_relative_path = 'images/nepal-govt.png'
    image_absolute_path = os.path.join(settings.BASE_DIR, 'static', image_relative_path)
    gov_logo = f'file://{image_absolute_path}'

    return {
        "serial_no": serial_no,
        "project": project,
        "officials": officials,
        "project_name": project.project_name,
        "gov_logo": gov_logo,  # 👉 Inject into context
    }
