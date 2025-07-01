# # projects/pdfs/first_installment/utils.py

# from projects.models.project import Project

# def build_pdf_context(serial_no, project_id):
#     try:
#         project = Project.objects.get(pk=project_id)

#         context = {
#             "project_name": project.project_name,
#             "fiscal_year": project.fiscal_year.year if project.fiscal_year else "",
#             "location": project.location or "-",
#             "budget": f"{project.budget} रू",
#             # You can add more context per serial_no
#         }

#         return context
#     except Project.DoesNotExist:
#         raise Http404("Project not found.")


from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.models.project import Project  # or wherever your Project model lives

def build_pdf_context(serial_no, project_id):
    project = Project.objects.get(serial_number=project_id)
    officials = OfficialDetail.objects.filter(project=project).order_by('serial_no')

    return {
        "serial_no": serial_no,
        "project": project,
        "officials": officials,
        # ... any other values used in the template
    }
