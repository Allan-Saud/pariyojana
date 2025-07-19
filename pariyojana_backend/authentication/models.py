from django.db import models
from projects.models.project import Project
from authentication.worker_model import Person
from django.contrib.auth import get_user_model

User = get_user_model()


class VerificationLog(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='verification_logs', null=True)
    file_title = models.CharField(max_length=255)
    uploader_role = models.CharField(max_length=100, blank=True, null=True)
    uploader_name = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.TextField(blank=True)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('checked', 'Checked'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    STATUS_CHOICES_NEPALI = {
    'pending': 'विचाराधीन',
    'checked': 'जाँच गरिएको',
    'approved': 'स्वीकृत',
    'rejected': 'अस्वीकृत', 
}
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    
    remarks = models.TextField(blank=True, null=True)
    checker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='verification_checked')
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='verification_approved')
    created_at = models.DateTimeField(auto_now_add=True)
    source_model = models.CharField(max_length=100) 
    source_id = models.IntegerField()
    
    
    def get_status_nepali(self):
        return VerificationLog.STATUS_CHOICES_NEPALI.get(self.status, self.status)