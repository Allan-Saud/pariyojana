# projects/models/monitoring_facilitation_committee.py

from django.db import models

class MonitoringFacilitationCommitteeMember(models.Model):
    GENDER_CHOICES = [("पुरुष", "पुरुष"), ("महिला", "महिला"), ("अन्य", "अन्य")]
    POST_CHOICES = [
        ("संयोजक", "संयोजक"),
        ("सदस्य सचिव", "सदस्य सचिव"),
        ("सदस्य", "सदस्य"),
    ]

    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name="monitoring_committee")
    serial_no = models.PositiveIntegerField()
    post = models.CharField(max_length=50, choices=POST_CHOICES)

    full_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    citizenship_no = models.CharField(max_length=100, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=True)

    citizenship_front = models.FileField(upload_to='monitoring_committee/citizenship/front/', null=True, blank=True)
    citizenship_back = models.FileField(upload_to='monitoring_committee/citizenship/back/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.project_id} - {self.serial_no} - {self.full_name}"
