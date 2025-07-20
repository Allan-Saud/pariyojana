# # signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models.Initiation_Process.initiation_process import InitiationProcess
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate  
from projects.models.project import Project
from authentication.models import VerificationLog 

@receiver(post_save, sender=InitiationProcess)
def update_project_status_on_confirmation(sender, instance, **kwargs):

    if instance.is_confirmed and instance.project.status != 'process_ensured':
        instance.project.status = 'process_ensured'
        instance.project.save()
# @receiver(post_save, sender=InitiationProcess)
# def update_project_status_on_confirmation(sender, instance, **kwargs):
#     if instance.is_confirmed and instance.project and instance.project.status != 'process_ensured':
#         instance.project.status = 'process_ensured'
#         instance.project.save()






@receiver(post_save, sender=MapCostEstimate)
def check_all_documents_approved(sender, instance, **kwargs):
    project = instance.project
    all_documents = project.map_cost_estimates.all()
    
    all_approved = all_documents.count() > 0 and all(
        doc.status == 'approved' for doc in all_documents
    )
    
    required_titles = [choice[0] for choice in MapCostEstimate.DOCUMENT_CHOICES]
    existing_titles = [doc.title for doc in all_documents]
    all_required_present = all(title in existing_titles for title in required_titles)
    
    if all_approved and all_required_present and project.status != 'completed':
        project.status = 'completed'
        project.save()


# @receiver(post_save, sender=MapCostEstimate)
# def create_verification_log_for_cost_estimate(sender, instance, created, **kwargs):
#     if created:
#         VerificationLog.objects.create(
#             project=instance.project,
#             file_title=f"Cost Estimate - {instance.title}",
#             status="pending",
#             source_model="CostEstimateDetail",
#             source_id=instance.id,
#             checker=instance.checker,  
#             approver=instance.approver,
#             uploader_role="अपलोड कर्ता"
#         )

@receiver(post_save, sender=MapCostEstimate)
def create_verification_log_for_cost_estimate(sender, instance, created, **kwargs):
    # Only create log if this is an update (not creation)
    # and checker and approver are both set
    if not created and instance.checker and instance.approver:
        # Check if VerificationLog already exists to avoid duplicates
        exists = VerificationLog.objects.filter(
            source_model="CostEstimateDetail",
            source_id=instance.id
        ).exists()
        if not exists:
            VerificationLog.objects.create(
                project=instance.project,
                file_title=f"Cost Estimate - {instance.title}",
                status=instance.status,
                source_model="CostEstimateDetail",
                source_id=instance.id,
                checker=instance.checker,
                approver=instance.approver,
                uploader_role="अपलोड कर्ता"
            )







# projects/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models.project import Project
from planning.PlanEntry.models import PlanEntry,PROJECT_TYPE_CHOICES
from notifications.utils import create_notification

@receiver(post_save, sender=Project)
def project_created_handler(sender, instance, created, **kwargs):
    if created:
        message = f"योजना '{instance.project_name}' हालै थपिएको छ। स्थिती: {dict(instance.STATUS_CHOICES).get(instance.status)}"
        create_notification(message, user=None) 

@receiver(post_save, sender=PlanEntry)
def plan_created_handler(sender, instance, created, **kwargs):
    if created:
        message = f"योजना प्रविष्टि '{instance.plan_name}' हालै थपिएको छ। योजना प्रकार: {dict(PROJECT_TYPE_CHOICES).get(instance.plan_type)}"
        create_notification(message, user=instance.created_by)
