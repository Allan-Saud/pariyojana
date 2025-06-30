from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
from projects.models.project import Project  # Ensure this import exists
from django.http import Http404
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
from projects.models.Consumer_Committee.official_detail import OfficialDetail


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

        return context
    
    if serial_no == 2:
        try:
            cost = CostEstimateDetail.objects.get(project=project)
        except CostEstimateDetail.DoesNotExist:
            cost = None

        try:
            agreement = ProjectAgreementDetails.objects.get(project=project)
        except ProjectAgreementDetails.DoesNotExist:
            agreement = None

        try:
            committee = ConsumerCommitteeDetail.objects.get(project=project)
        except ConsumerCommitteeDetail.DoesNotExist:
            committee = None

        try:
           chairperson = OfficialDetail.objects.filter(project=project, post="अध्यक्ष").first()
        except OfficialDetail.DoesNotExist:
            chairperson = None

        context = {
            "project_name": project.project_name,
            "ward_no": project.ward_no,
            "estimated_cost": cost.estimated_cost if cost else None,
            "municipality_amount": agreement.municipality_amount if agreement else None,
            "consumer_committee_name": committee.consumer_committee_name if committee else None,
            "chairperson_name": chairperson.full_name if chairperson else None,
        }

        return context
    
    
    if serial_no == 3:
            try:
                agreement = ProjectAgreementDetails.objects.get(project=project)
            except ProjectAgreementDetails.DoesNotExist:
                agreement = None

            context = {
                "project_name": project.project_name,
                "address":project.location,
                "ward_no": project.ward_no,
                "municipality_amount": agreement.municipality_amount if agreement else None,
            }

            return context
        
    if serial_no == 4:
        context = {
            "project_name": project.project_name,
            "ward_no": project.ward_no,
            "location": getattr(project, 'location', None),
        }
        return context



    else:
        raise NotImplementedError(f"Serial number {serial_no} not yet implemented.")
    
    
