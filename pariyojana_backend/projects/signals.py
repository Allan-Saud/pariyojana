# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from projects.models.Initiation_Process import initiation_process

# @receiver(post_save, sender=initiation_process)
# def update_project_status_on_confirmation(sender, instance, **kwargs):
#     if instance.is_confirmed and instance.project.status != 'process_ensured':
#         instance.project.status = 'process_ensured'
#         instance.project.save()
print("✅ projects/signals.py loaded")
from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models.Initiation_Process.initiation_process import InitiationProcess
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate  # Add this import
from projects.models.project import Project
from authentication.models import VerificationLog  # Add this import

@receiver(post_save, sender=InitiationProcess)
def update_project_status_on_confirmation(sender, instance, **kwargs):

    if instance.is_confirmed and instance.project.status != 'process_ensured':
        instance.project.status = 'process_ensured'
        instance.project.save()
        print("✅ Project status updated to process_ensured")



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


@receiver(post_save, sender=MapCostEstimate)
def create_verification_log_for_cost_estimate(sender, instance, created, **kwargs):
    if created:
        VerificationLog.objects.create(
            project=instance.project,
            file_title=f"Cost Estimate - {instance.title}",
            status="pending",
            source_model="CostEstimateDetail",
            source_id=instance.id,
            checker=instance.checker,  # Make sure these fields exist
            approver=instance.approver,
            uploader_role="अपलोड कर्ता"
        )