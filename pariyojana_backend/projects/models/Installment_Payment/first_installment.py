from django.db import models
from django.utils import timezone

class FirstInstallmentDocument(models.Model):
    SERIAL_CHOICES = (
        (1, '१'),
        (2, '२'),
        (3, '३'),
    )

    serial_number = models.PositiveSmallIntegerField(choices=SERIAL_CHOICES, unique=True)
    file = models.FileField(upload_to='installment_files/', null=True, blank=True)
    remarks = models.TextField(blank=True)
    uploaded_at = models.DateField(default=timezone.now)

    def status(self):
        return "अपलोड गरिएको" if self.file else ""
