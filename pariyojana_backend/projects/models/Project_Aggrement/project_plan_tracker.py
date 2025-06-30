from django.db import models
from projects.models.project import Project  # Adjust import path if needed

class ProjectPlanTrackerUpload(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='plan_tracker_uploads',null=True)
    serial_no = models.PositiveIntegerField()
    file = models.FileField(upload_to='project_plan_tracker_uploads/')
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'serial_no')  # One file per project per serial_no

    def __str__(self):
        return f"Upload for project {self.project.serial_number}, item {self.serial_no}"
