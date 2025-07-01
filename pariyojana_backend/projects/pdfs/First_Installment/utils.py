from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.models.project import Project  # or wherever your Project model lives

def build_pdf_context(serial_no, project_id):
    project = Project.objects.get(serial_number=project_id)
    officials = OfficialDetail.objects.filter(project=project).order_by('serial_no')

    return {
        "serial_no": serial_no,
        "project": project,
        "officials": officials,
        "project_name":project.project_name
    
    }
