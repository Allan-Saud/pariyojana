from projects.models.project import Project

def build_pdf_context(serial_no, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Exception("Project not found.")

    context = {
        "project_name": project.project_name,
        "location": project.location or "",
        "fiscal_year": project.fiscal_year.year if project.fiscal_year else "",
        "budget":project.budget
    }

    return context
