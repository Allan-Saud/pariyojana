from django.db import models
from django.utils import timezone

class ConsumerCommitteeUpload(models.Model):
    serial_no = models.PositiveIntegerField(unique=True)
    file = models.FileField(upload_to='consumer_committee_uploads/')
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload for item {self.serial_no}"
