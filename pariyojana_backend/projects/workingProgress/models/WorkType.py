from django.db import models
from projects.models.project import Project
from project_settings.models.unit import Unit

class WorkType(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='work_types')
    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.unit})"
