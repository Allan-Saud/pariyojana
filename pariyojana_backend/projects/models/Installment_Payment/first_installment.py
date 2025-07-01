# projects/models/Installment_Payment/first_installment.py
from django.db import models
from projects.models.project import   Project
class FirstInstallmentUpload(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='first_installments',null=True)
    serial_no = models.PositiveIntegerField(unique=True)
    file = models.FileField(upload_to='first_installment_uploads/')
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"First Installment - Serial {self.serial_no}"
