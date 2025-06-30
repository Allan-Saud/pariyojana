from django.db import models
from projects.models.project import Project

class ProjectAgreementWorkorderUpload(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_aggrement_workorder', null=True)
    serial_no = models.PositiveIntegerField(unique=True)
    file = models.FileField(upload_to='project_agreement_workorder_uploads/')
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload for item {self.serial_no}"
