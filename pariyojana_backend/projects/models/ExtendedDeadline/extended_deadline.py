from django.db import models
from django.contrib.auth import get_user_model
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails

User = get_user_model()

class ExtendedDeadline(models.Model):
    agreement = models.ForeignKey(
        ProjectAgreementDetails,
        on_delete=models.CASCADE,
        related_name='extensions'
    )

    previous_completion_date = models.DateField("अघिल्लो सम्पन्न मिति")
    extended_completion_date = models.DateField("नयाँ सम्पन्न मिति")
    reason = models.TextField("म्याद थप गर्ने कारण", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set the previous date if not already set
        if not self.previous_completion_date:
            self.previous_completion_date = self.agreement.completion_date

        # Update the agreement's current completion date
        self.agreement.completion_date = self.extended_completion_date
        self.agreement.save(update_fields=['completion_date'])

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Extension for Project {self.agreement.project.id} to {self.extended_completion_date}"
