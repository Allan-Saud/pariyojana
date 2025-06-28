from django.db import models
from django.utils import timezone
from projects.models.project import Project  

class BankAccountRecommendation(models.Model):
    TITLE_CHOICES = [
        ('बैंक खाता सञ्चालन सिफारिस', 'बैंक खाता सञ्चालन सिफारिस'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bank_recommendations')
    title = models.CharField(max_length=255, choices=TITLE_CHOICES, default='बैंक खाता सञ्चालन सिफारिस')
    date = models.DateField(default=timezone.localdate)
    status = models.CharField(max_length=100, blank=True)  # Auto-set based on file

    file = models.FileField(upload_to='bank_recommendation/', null=True, blank=True)
    remark = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically update status based on file
        if self.file:
            self.status = "अपलोड गरिएको"
        else:
            self.status = ""
        super().save(*args, **kwargs)

    def soft_delete(self):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} ({self.project})"
