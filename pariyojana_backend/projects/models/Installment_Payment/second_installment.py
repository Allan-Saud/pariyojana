from django.db import models
from django.utils import timezone
from projects.models.project import Project

class SecondInstallment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='second_installments')
    serial_no = models.PositiveIntegerField()
    file = models.FileField(upload_to='second_installment_uploads/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'serial_no')

    def __str__(self):
        return f"Second Installment {self.serial_no} for Project {self.project.serial_number}"