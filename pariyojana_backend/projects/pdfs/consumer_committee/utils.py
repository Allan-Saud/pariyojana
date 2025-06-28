def build_pdf_context(serial_no, project_id):
    from projects.models.project import Project
    from pariyojana_backend.projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
    from pariyojana_backend.projects.models.Initiation_Process.initiation_process import InitiationProcess

    try:
        project = Project.objects.select_related("fiscal_year", "expenditure_center").get(pk=project_id)
    except Project.DoesNotExist:
        raise Exception("Project not found.")

    # Try to get a ConsumerCommitteeDetail manually (assuming one entry per project)
    consumer_committee_details = ConsumerCommitteeDetail.objects.first()  # Fallback: fetch latest

    context = {
        "fiscal_year": project.fiscal_year.year if project.fiscal_year else "",
        "project_name": project.project_name,
        "location": project.location if hasattr(project, "location") else "",
        "total_cost": project.budget,

        "chairman_name": consumer_committee_details.consumer_committee_name if consumer_committee_details else "",
        "contact_number": consumer_committee_details.contact_no if consumer_committee_details else "",
    }

    return context
