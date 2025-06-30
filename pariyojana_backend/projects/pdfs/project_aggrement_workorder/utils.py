from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
from projects.models.project import Project  # Ensure this import exists
from django.http import Http404

def build_pdf_context(serial_no: int, project_serial_number: int):
    try:
        project = Project.objects.get(serial_number=project_serial_number)
    except Project.DoesNotExist:
        raise Http404("Project not found.")

    if serial_no == 1:
        try:
            agreement = ProjectAgreementDetails.objects.get(project=project)
        except ProjectAgreementDetails.DoesNotExist:
            agreement = None

        context = {
            "project_name": project.project_name,
            "ward_no": project.ward_no,
            "fiscal_year": getattr(project, 'fiscal_year', ''),  
            "budget": getattr(project, 'budget', ''),
            "municipality_percentage": agreement.municipality_percentage if agreement else None,
            "public_participation_percentage": agreement.public_participation_percentage if agreement else None,
            "public_participation_amount": agreement.public_participation_amount if agreement else None,
        }
        print("Context for serial_no=1:", context)
        return context
    else:
        raise NotImplementedError(f"Serial number {serial_no} not yet implemented.")
