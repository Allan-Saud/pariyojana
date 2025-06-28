from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from projects.models.project import Project
from projects.models.Installment_Payment.bankaccount_recommendation import BankAccountRecommendation

class AccountPhoto(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='account_photo')
    bank_account_number = models.CharField(max_length=50)
    # This will be fetched from related BankAccountRecommendation (not uploaded directly here)
    check_photo = models.FileField(
        upload_to='account_check_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        null=True,
        blank=True
    )

    # Optional link to fetch file from recommendation
    recommendation = models.OneToOneField(
        BankAccountRecommendation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='linked_account_photo'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.recommendation and self.recommendation.file:
            self.check_photo = self.recommendation.file
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bank Photo for Project {self.project.id}"
