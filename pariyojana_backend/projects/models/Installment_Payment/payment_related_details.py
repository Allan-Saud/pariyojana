from django.db import models
from projects.models.project import Project  # assuming your main model is here
from django.utils import timezone

class PaymentRelatedDetail(models.Model):
    TITLE_CHOICES = [
        ('पहिलो पेश्की भुक्तानी', 'पहिलो पेश्की भुक्तानी'),
        ('दोस्रो किस्ता भुक्तानी', 'दोस्रो किस्ता भुक्तानी'),
        ('अन्तिम किस्ता भुक्तानी', 'अन्तिम किस्ता भुक्तानी'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="payment_details")
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    issue_date = models.DateField(default=timezone.localdate,null=True,blank=True)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    payment_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    physical_progress = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    uploaded_file = models.FileField(upload_to='payment_related_files/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
