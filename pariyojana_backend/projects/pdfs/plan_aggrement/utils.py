# from django.http import Http404
# from projects.models.project import Project
# from projects.models.Program_Details.program_detail import ProgramDetail
# from projects.models.Consumer_Committee.official_detail import OfficialDetail
# from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember
# from datetime import date
# from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
# from django.conf import settings
# import os

# def build_pdf_context(serial_no: int, project_serial_number: int):
#     try:
#         project = Project.objects.get(serial_number=project_serial_number)
#     except Project.DoesNotExist:
#         raise Http404("Project not found.")

#     if serial_no == 1:
#         officials = OfficialDetail.objects.filter(project=project).order_by("serial_no")
        
#         attendance_rows = []
#         for official in officials:
#             attendance_rows.append({
#                 "post": official.post,
#                 "name": f"श्री {official.full_name}",
#                 "signature": "",
#             })
#         logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'nepal-govt.png')
#         context = {
            
#             'logo_path': f'file://{logo_path}',
#             "meeting_date": "20...... साल....महिना......",
#             "meeting_location": "पुल्चोक, ललितपुर बागमती प्रदेश, नेपाल",
#             "chairperson_name": officials.filter(post="अध्यक्ष").first().full_name if officials.filter(post="अध्यक्ष").exists() else "........",

#             "attendance_rows": attendance_rows,

#             "agenda_list": [
#                 "बैंक खाता खोल्ने सम्बन्धमा ।",
#                 "बैंक खातामा हस्ताक्षर सम्बन्धमा ।",
#                 "अख्तियारी सम्बन्धमा ।",
#                 "जनश्रमदान सम्बन्धमा ।",
#             ],

#             "decision_list": [
#                 "बैठकको कार्यसूची नं.१ को सम्बन्धमा छलफल हुँदा बैंकमा यस उपभोक्ता समितिको खाता खोल्ने निर्णय गर्दै खाता खोल्न वडा कार्यालयमा सिफारिस माग गर्ने निर्णय गरियो।",
#                 "बैठकको कार्यसूची नं.२ को सम्बन्धमा छलफल हुँदा बैंक खातामा अध्यक्ष/सचिव/कोषाध्यक्षको अनिवार्य हस्ताक्षर संयुक्त रुपमा प्रयोग गर्ने निर्णय गरियो।",
#                 "बैठकको कार्यसूची नं.३ को सम्बन्धमा छलफल हुँदा योजना सम्झौता गर्ने अख्तियारी अध्यक्ष/सचिव/कोषाध्यक्षलाई दिने र किस्ता रकम माग गर्ने लगायतका चिठी पत्र आदान प्रदान गर्ने अख्तियारी समेत अध्यक्ष/सचिव/कोषाध्यक्षलाई प्रदान गर्ने निर्णय गरियो।",
#                 "बैठकको कार्यसूची नं.४ को सम्बन्धमा छलफल हुँदा महानगरपालिकाको नीति अनुसार यस योजनाको लागि न्यूनतम १० प्रतिशत बराबरको रकम नगदै दाखिला गर्ने निर्णय गरियो।",
#             ]
#         }
#         return context

#     elif serial_no == 2:
   
#             project_name = project.project_name or "........"
#             budget = project.budget or "........"  

#             members = MonitoringFacilitationCommitteeMember.objects.filter(project=project).order_by("serial_no")

#             committee_members = [
#                 {"post": member.post, "name": member.full_name}
#                 for member in members
#             ]

#             context = {
#                 "project_name": project_name,
#                 "budget": budget,
#                 "committee_members": committee_members,
#             }

#             return context
        
        
        
#     elif serial_no == 4:
#         officials = OfficialDetail.objects.filter(project=project).order_by("serial_no")

      
#         attendance_rows = []
#         for official in officials:
#             attendance_rows.append({
#                 "post": official.post,
#                 "name": f"श्री {official.full_name}",
#                 "signature": "",  
#             })

       
#         chairpersons = [
#             {"name": f"श्री {official.full_name}", "post": official.post}
#             for official in officials if official.post == "अध्यक्ष"
#         ]

    
#         project_name = getattr(project, 'name', None) or getattr(project, 'project_name', None) or "........"

#         context = {
#             "project_name": project_name,
#             "chairpersons": chairpersons,
#             # ...
#         }
        
#         print(f"Serial 4 officials count: {officials.count()}")
#         for official in officials:
#             print(f"Official: post={official.post}, full_name={official.full_name}")

#         return context
    
    
#     elif serial_no == 5:
#         return {
#             "message": "No specific data needed for serial_no 5.",
#             "project_name": getattr(project, 'project_name', '........')
#         }
        

#     if serial_no == 6:
    
#         context = {
#             "project_name": getattr(project, 'project_name', '........'),
#             "ward_no": project.ward_no or "........",
#             "agreement_date": date.today().strftime('%Y-%m-%d'),  
#             "prepared_by": "........",  
#             "position": "........",
#         }
#         return context

#     elif serial_no == 7:
#         try:
#             consumer_committee = ConsumerCommitteeDetail.objects.get(project=project)
#             consumer_name = consumer_committee.consumer_committee_name
#         except ConsumerCommitteeDetail.DoesNotExist:
#             consumer_name = "........"

#         context = {
#             "project_name": project.project_name,
#             "consumer_name": consumer_name,
#             "ward_no": project.ward_no,
#             "tippani_date": date.today().strftime("%Y-%m-%d"),
#             "recommendation_by": "........",
#             "position": "........",
#             "remarks": "सम्पूर्ण प्रक्रिया पूरा भएको देखिएकोले उपभोक्ता समितिलाई कार्यादेश दिन सिफारिस गरिन्छ।"
#         }
#         return context

#     else:
#         raise NotImplementedError(f"Serial number {serial_no} not yet implemented.")
from django.http import Http404
from projects.models.project import Project
from projects.models.Program_Details.program_detail import ProgramDetail
from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember
from datetime import date
from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
from django.conf import settings
import os

def build_pdf_context(serial_no: int, project_serial_number: int):
    try:
        project = Project.objects.get(serial_number=project_serial_number)
    except Project.DoesNotExist:
        raise Http404("Project not found.")

    # ✅ Define the logo path once for all contexts
    gov_logo = f'file://{os.path.join(settings.BASE_DIR, "static/images/nepal-govt.png")}'

    if serial_no == 1:
        officials = OfficialDetail.objects.filter(project=project).order_by("serial_no")
        attendance_rows = [
            {"post": o.post, "name": f"श्री {o.full_name}", "signature": ""}
            for o in officials
        ]

        context = {
            "gov_logo": gov_logo,  # ✅ Added here
            "meeting_date": "20...... साल....महिना......",
            "meeting_location": "पुल्चोक, ललितपुर बागमती प्रदेश, नेपाल",
            "chairperson_name": officials.filter(post="अध्यक्ष").first().full_name if officials.filter(post="अध्यक्ष").exists() else "........",
            "attendance_rows": attendance_rows,
            "agenda_list": [
                "बैंक खाता खोल्ने सम्बन्धमा ।",
                "बैंक खातामा हस्ताक्षर सम्बन्धमा ।",
                "अख्तियारी सम्बन्धमा ।",
                "जनश्रमदान सम्बन्धमा ।",
            ],
            "decision_list": [
                "बैठकको कार्यसूची नं.१ को सम्बन्धमा छलफल हुँदा बैंकमा यस उपभोक्ता समितिको खाता खोल्ने निर्णय गर्दै खाता खोल्न वडा कार्यालयमा सिफारिस माग गर्ने निर्णय गरियो।",
                "बैठकको कार्यसूची नं.२ को सम्बन्धमा छलफल हुँदा बैंक खातामा अध्यक्ष/सचिव/कोषाध्यक्षको अनिवार्य हस्ताक्षर संयुक्त रुपमा प्रयोग गर्ने निर्णय गरियो।",
                "बैठकको कार्यसूची नं.३ को सम्बन्धमा छलफल हुँदा योजना सम्झौता गर्ने अख्तियारी अध्यक्ष/सचिव/कोषाध्यक्षलाई दिने र किस्ता रकम माग गर्ने लगायतका चिठी पत्र आदान प्रदान गर्ने अख्तियारी समेत अध्यक्ष/सचिव/कोषाध्यक्षलाई प्रदान गर्ने निर्णय गरियो।",
                "बैठकको कार्यसूची नं.४ को सम्बन्धमा छलफल हुँदा महानगरपालिकाको नीति अनुसार यस योजनाको लागि न्यूनतम १० प्रतिशत बराबरको रकम नगदै दाखिला गर्ने निर्णय गरियो।",
            ]
        }
        return context

    elif serial_no == 2:
        members = MonitoringFacilitationCommitteeMember.objects.filter(project=project).order_by("serial_no")
        committee_members = [{"post": m.post, "name": m.full_name} for m in members]

        context = {
            "gov_logo": gov_logo,  # ✅ Added here
            "project_name": project.project_name or "........",
            "budget": project.budget or "........",
            "committee_members": committee_members,
        }
        return context
    
    elif serial_no == 3:
        # Example: Use ProgramDetail or any model relevant for serial 3
        program_details = ProgramDetail.objects.filter(project=project)
        
        program_rows = [{"name": p.program_name} for p in program_details]

        context = {
            "gov_logo": gov_logo,
            "project_name": project.project_name or "........",
            "program_rows": program_rows,
        }
        return context


    elif serial_no == 4:
        officials = OfficialDetail.objects.filter(project=project).order_by("serial_no")
        attendance_rows = [{"post": o.post, "name": f"श्री {o.full_name}", "signature": ""} for o in officials]
        chairpersons = [{"name": f"श्री {o.full_name}", "post": o.post} for o in officials if o.post == "अध्यक्ष"]

        context = {
            "gov_logo": gov_logo,  # ✅ Added here
            "project_name": getattr(project, 'name', None) or getattr(project, 'project_name', None) or "........",
            "chairpersons": chairpersons,
            "attendance_rows": attendance_rows,
        }

        print(f"Serial 4 officials count: {officials.count()}")
        for o in officials:
            print(f"Official: post={o.post}, full_name={o.full_name}")

        return context

    elif serial_no == 5:
        return {
            "gov_logo": gov_logo,  # ✅ Added here
            "message": "No specific data needed for serial_no 5.",
            "project_name": getattr(project, 'project_name', '........')
        }

    elif serial_no == 6:
        return {
            "gov_logo": gov_logo,  # ✅ Added here
            "project_name": getattr(project, 'project_name', '........'),
            "ward_no": project.ward_no or "........",
            "agreement_date": date.today().strftime('%Y-%m-%d'),
            "prepared_by": "........",
            "position": "........",
        }

    elif serial_no == 7:
        try:
            consumer_committee = ConsumerCommitteeDetail.objects.get(project=project)
            consumer_name = consumer_committee.consumer_committee_name
        except ConsumerCommitteeDetail.DoesNotExist:
            consumer_name = "........"

        return {
            "gov_logo": gov_logo,  # ✅ Added here
            "project_name": project.project_name,
            "consumer_name": consumer_name,
            "ward_no": project.ward_no,
            "tippani_date": date.today().strftime("%Y-%m-%d"),
            "recommendation_by": "........",
            "position": "........",
            "remarks": "सम्पूर्ण प्रक्रिया पूरा भएको देखिएकोले उपभोक्ता समितिलाई कार्यादेश दिन सिफारिस गरिन्छ।"
        }

    else:
        raise NotImplementedError(f"Serial number {serial_no} not yet implemented.")






    
        
    
    
    
    
