# projects/models/initiation_process.py

from django.db import models

class InitiationProcess(models.Model):
    INITIATION_CHOICES = [
        ("उपभोक्ता समिति मार्फत", "उपभोक्ता समिति मार्फत"),
        ("सिलबन्दि दरभाउपत्र मार्फत", "सिलबन्दि दरभाउपत्र मार्फत"),
        ("बोलपत्र मार्फत", "बोलपत्र मार्फत"),
        ("अमानत मार्फत", "अमानत मार्फत"),
        ("सोझै खरिद", "सोझै खरिद"),
    ]

    project = models.OneToOneField("projects.Project", on_delete=models.CASCADE,null=True)
    initiation_method = models.CharField(max_length=100, choices=INITIATION_CHOICES)
    is_confirmed = models.BooleanField(default=False)  # when OK is clicked
    started_at = models.DateTimeField(null=True, blank=True)

    # Flags for enabling steps
    has_consumer_committee = models.BooleanField(default=False)
    has_agreement = models.BooleanField(default=False)
    has_payment_installment = models.BooleanField(default=False)

    def initiate_project(self):
        from django.utils import timezone
        self.started_at = timezone.now()
        self.has_consumer_committee = True
        self.has_agreement = True
        self.has_payment_installment = True
        self.save()
