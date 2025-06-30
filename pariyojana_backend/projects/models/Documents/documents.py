from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models.project import Project

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents',null=True)
    title = models.CharField(max_length=255)  # फायलको नाम
    file = models.FileField(upload_to='uploads/documents/')  # फाइल अपलोड
    remarks = models.TextField(blank=True, null=True)  # कैफियत
    uploaded_at = models.DateTimeField(auto_now_add=True)  # अपलोड मिति
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title
