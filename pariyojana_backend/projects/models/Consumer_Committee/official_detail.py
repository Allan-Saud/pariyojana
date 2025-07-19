# projects/models/official_detail.py

from django.db import models
class OfficialDetail(models.Model):
    GENDER_CHOICES = [("पुरुष", "पुरुष"), ("महिला", "महिला"), ("अन्य", "अन्य")]
    POST_CHOICES = [
        ("अध्यक्ष", "अध्यक्ष"),
        ("सचिव", "सचिव"),
        ("कोषाध्यक्ष", "कोषाध्यक्ष"),
        ("सदस्य", "सदस्य"),
    ]

    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name="officials")

    serial_no = models.PositiveIntegerField(null=True, blank=True)
    post = models.CharField(max_length=50, choices=POST_CHOICES, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    citizenship_no = models.CharField(max_length=100, null=True, blank=True)

    citizenship_front = models.FileField(upload_to='officials/citizenship/front/', null=True, blank=True)
    citizenship_back = models.FileField(upload_to='officials/citizenship/back/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_id} - {self.serial_no} - {self.full_name}"

