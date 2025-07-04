# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models.Initiation_Process import initiation_process

@receiver(post_save, sender=initiation_process)
def update_project_status_on_confirmation(sender, instance, **kwargs):
    if instance.is_confirmed and instance.project.status != 'process_ensured':
        instance.project.status = 'process_ensured'
        instance.project.save()
