from django.db import models
from django.utils import timezone
from projects.models.project import Project
class ConsumerCommitteeUpload(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="consumer_uploads",null=True,blank=True)
    serial_no = models.PositiveIntegerField()
    file = models.FileField(upload_to='consumer_committee_uploads/')
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        unique_together = ('project', 'serial_no')  # ✅ ensures serial_no is unique per project

    def __str__(self):
        return f"Upload for project {self.project_id} - item {self.serial_no}"

