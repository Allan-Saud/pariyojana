from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models.project import Project
from projects.models.progress_stage import ProjectProgress

DEFAULT_PROGRESS_STEPS = [
    ("cost_estimate_approved", "लागत अनुमान स्वीकृत"),
    ("beneficiary_analysis", "आयोजनाबाट लाभान्वित हुनेको विवरण"),
    ("ward_notice", "आम भेला गर्न वडा कार्यालयको सूचना"),
    ("committee_formed", "उपभोक्ता समिति गठन"),
    ("site_photo", "योजना स्थलको काम सुरु नभएको फोटो"),
    ("agreement_sent", "योजना सम्झौता सिफारिस"),
    ("agreement_done", "योजना सम्झौता तथा कार्यादेश"),
    ("payment_1", "पहिलो किस्ता भुक्तानी"),
    ("payment_2", "दोस्रो किस्ता भुक्तानी"),
    ("payment_final", "अन्तिम किस्ता भुक्तानी"),
    ("handover", "आयोजना हस्तान्तरण"),
]

@receiver(post_save, sender=Project)
def create_default_progress_stages(sender, instance, created, **kwargs):
    if created:
        for key, label in DEFAULT_PROGRESS_STEPS:
            ProjectProgress.objects.create(
                project=instance,
                stage_key=key,
                stage_label=label,
                is_completed=False
            )
