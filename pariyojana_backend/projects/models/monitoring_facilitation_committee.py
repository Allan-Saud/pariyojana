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
    
    serial_no = models.PositiveIntegerField()  # क्र.स
    post = models.CharField(max_length=50, choices=POST_CHOICES)  # पद
    full_name = models.CharField(max_length=255)  # नाम थर
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # लिंग
    address = models.CharField(max_length=255)  # ठेगाना
    citizenship_no = models.CharField(max_length=100)  # नागरिकता प्र. नं.
    contact_no = models.CharField(max_length=20)  # सम्पर्क नं

    citizenship_front = models.FileField(upload_to='monitoring_committee/citizenship/front/')
    citizenship_back = models.FileField(upload_to='monitoring_committee/citizenship/back/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_id} - {self.serial_no} - {self.full_name}"
