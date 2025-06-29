from django.db import models
from projects.models.project import Project

class ProjectProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress')
    stage_key = models.CharField(max_length=100)  # e.g. 'cost_estimate_approved'
    stage_label = models.CharField(max_length=255)  # e.g. 'लागत अनुमान स्वीकृत'
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('project', 'stage_key')

    def __str__(self):
        return f"{self.project.project_name} - {self.stage_label} ({'Done' if self.is_completed else 'Pending'})"

