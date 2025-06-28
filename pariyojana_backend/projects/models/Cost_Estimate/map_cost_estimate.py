from django.db import models
from django.utils import timezone
from projects.models.project import Project
from authentication.worker_model import Person  # Assuming worker info is here

class MapCostEstimate(models.Model):
    DOCUMENT_CHOICES = [
        ('सम्भव्यता अध्यायन प्रतिवेदन', 'सम्भव्यता अध्यायन प्रतिवेदन'),
        ('नक्सा', 'नक्सा'),
        ('लागत अनुमान (लागत इष्टिमेट)', 'लागत अनुमान (लागत इष्टिमेट)'),
        ('प्राविधिक प्रतिवेदन', 'प्राविधिक प्रतिवेदन'),
        ('निर्माण कार्य तालिका', 'निर्माण कार्य तालिका'),
        ('लागत अनुमान स्विकृती सम्बन्धी टिप्पणी आदेश', 'लागत अनुमान स्विकृती सम्बन्धी टिप्पणी आदेश'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='map_cost_estimates')
    title = models.CharField(max_length=255, choices=DOCUMENT_CHOICES)
    date = models.DateField(default=timezone.localdate)
    file = models.FileField(upload_to='map_cost_estimates/', null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=100, default='', blank=True)  # अपलोड गरिएको, चेक जाँचको लागि पठाइएको

    # प्रमाणिकरण info
    checker = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_docs')
    approver = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_docs')

    is_verified = models.BooleanField(default=False)  # If प्रमाणिकरण is done
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
