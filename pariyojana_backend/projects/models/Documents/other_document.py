from django.db import models
from projects.models.project import Project

class OtherDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    serial_no = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'serial_no')
