def build_pdf_context(serial_no, project_id):
    from projects.models.project import Project
    from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
    from projects.models.Consumer_Committee.official_detail import OfficialDetail
    from projects.models.Project_Aggrement.project_aggrement_details import  ProjectAgreementDetails
    from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
    

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Exception("Project not found.")

    committee = ConsumerCommitteeDetail.objects.filter(project=project).first()
    officials = OfficialDetail.objects.filter(project=project).order_by('serial_no')
    agreement = ProjectAgreementDetails.objects.filter(project=project).first()
    cost_estimate = CostEstimateDetail.objects.filter(project=project).first()
    chairman_name = "-"
    secretary_name = "-"

    for official in officials:
        if official.post == "अध्यक्ष":
            chairman_name = official.full_name
        elif official.post == "सचिव":
            secretary_name = official.full_name

    context = {
        "project_name": project.project_name,
        "ward_number":project.ward_no,
        "fiscal_year": project.fiscal_year.year if project.fiscal_year else "",
        "location": project.location or "-",
        "total_cost": f"{project.budget}",
        "budget_title": project.source.name if project.source else "-",
        "agreement_date": project.created_at.date() if project.created_at else "-",
        "completion_date": project.updated_at.date() if project.updated_at else "-",
        "chairman_name": committee.representative_name if committee else "-",
        "contact_number": committee.contact_no if committee else "-",
        "officials": officials,
        "municipality_amount": agreement.municipality_amount if agreement else 0,
        "public_participation_amount": agreement.public_participation_amount if agreement else 0,
        "consumer_committee_name": committee.consumer_committee_name if committee else "-",
        "estimated_cost": cost_estimate.estimated_cost if cost_estimate else 0,
        "work_order_date": agreement.work_order_date if agreement else None,
        "end_date": agreement.completion_date if agreement else None,
        "chairman_name": chairman_name,
        "secretary_name": secretary_name,
    }

    # # Add serial-specific context if needed
    # if serial_no == 1:
    #     context["meeting_date"] = "-"
    #     context["decisions"] = []
    # elif serial_no == 3:
    #     context["photos"] = [] 

    return context