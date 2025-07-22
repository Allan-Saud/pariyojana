import nepali_datetime as ndt
def build_pdf_context(serial_no, project_id):
    from projects.models.project import Project
    from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
    from projects.models.Initiation_Process.initiation_process import InitiationProcess
    from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails
    from projects.models.Consumer_Committee.official_detail import OfficialDetail
    from django.utils import timezone

    try:
        project = Project.objects.select_related(
            "fiscal_year", 
            "expenditure_center",
            "source"
        ).get(pk=project_id)
    except Project.DoesNotExist:
        raise Exception("Project not found.")

    # Get related data
    consumer_committee_details = ConsumerCommitteeDetail.objects.filter(project=project).first()
    project_agreement = ProjectAgreementDetails.objects.filter(project=project).first()
    initiation_process = InitiationProcess.objects.filter(project=project).first()
    
    # Get officials
    chairman = OfficialDetail.objects.filter(project=project, post="अध्यक्ष").first()
    secretary = OfficialDetail.objects.filter(project=project, post="सचिव").first()

    # Nepali date conversion (you may need to implement this properly)
    current_nepali_date = "२०८० साल असोज १५ गते"  # Placeholder - implement Nepali date conversion

    context = {
        "fiscal_year": project.fiscal_year.year if project.fiscal_year else "",
        "project_name": project.project_name,
        "location": project.location if hasattr(project, "location") else "",
        "total_cost": f"{project.budget:,} रू" if project.budget else "० रू",
        "budget_title": project.source.name if project.source else "",
        "work_description": project.description if project.description else "",
        
        # Consumer committee details
        "consumer_committee_name": consumer_committee_details.consumer_committee_name if consumer_committee_details else "",
        "chairman_name": chairman.full_name if chairman else "",
        "secretary_name": secretary.full_name if secretary else "",
        "contact_number": consumer_committee_details.contact_no if consumer_committee_details else "",
        
        # Project timeline
        # "agreement_date": project_agreement.agreement_date.strftime("%Y-%m-%d") if project_agreement and project_agreement.agreement_date else "",
        # "start_date": initiation_process.start_date.strftime("%Y-%m-%d") if initiation_process and initiation_process.start_date else "",
        # "completion_date": initiation_process.completion_date.strftime("%Y-%m-%d") if initiation_process and initiation_process.completion_date else "",
        "agreement_date": ndt.date.from_datetime_date(project_agreement.agreement_date).strftime("%K-%n-%D") + " गते" if project_agreement and project_agreement.agreement_date else "",
        "start_date": ndt.date.from_datetime_date(initiation_process.start_date).strftime("%K-%n-%D") + " गते" if initiation_process and initiation_process.start_date else "",
        "completion_date": ndt.date.from_datetime_date(initiation_process.completion_date).strftime("%K-%n-%D") + " गते" if initiation_process and initiation_process.completion_date else "",
        "current_date": ndt.date.today().strftime("%K-%n-%D") + " गते",
        # # Current date
        # "current_date": current_nepali_date,
        
        # Execution method (you may need to get this from your model)
        "execution_method": "उपभोक्ता समितिद्वारा सम्पादन",
        
        # Duration calculation
        "duration": self._calculate_duration(initiation_process) if initiation_process else "",
    }

    # Add serial-specific context
    if serial_no == 7:
        context.update({
            "estimate_approval_date": current_nepali_date,
            "committee_decision": "समितिको बैठकले यस परियोजनाको अनुमानित लागत तथा कार्ययोजना विचार गरी स्वीकृत गर्दछ।",
            "additional_remarks": project_agreement.remarks if project_agreement else ""
        })

    return context

def _calculate_duration(self, initiation_process):
    if initiation_process.start_date and initiation_process.completion_date:
        delta = initiation_process.completion_date - initiation_process.start_date
        months = delta.days // 30
        days = delta.days % 30
        if months > 0:
            return f"{months} महिना {days} दिन"
        return f"{days} दिन"
    return ""