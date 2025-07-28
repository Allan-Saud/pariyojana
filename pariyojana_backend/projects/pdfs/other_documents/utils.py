import os
from django.conf import settings
from projects.models.project import Project

def build_pdf_context(serial_no, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Exception("Project not found.")

    # ✅ Absolute file path for the government logo
    gov_logo = f'file://{os.path.join(settings.BASE_DIR, "static/images/nepal-govt.png")}'

    context = {
        "serial_no": serial_no,
        "project_name": project.project_name,
        "location": project.location or "",
        "fiscal_year": project.fiscal_year.year if project.fiscal_year else "",
        "budget": project.budget,
        "gov_logo": gov_logo,  # ✅ Added the logo to the context
    }

    return context
