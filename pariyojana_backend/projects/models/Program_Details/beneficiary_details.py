from django.db import models
from projects.models.Program_Details.program_detail import ProgramDetail

class BeneficiaryDetail(models.Model):
    CATEGORY_CHOICES = [
        ('total_households', 'जम्मा परिवार'),
        ('total_population', 'जम्मा जनसंख्या'),
        ('indigenous_families', 'आदिवासी जनजातिको परिवार संख्या'),
        ('dalit_families', 'दलित वर्गको परिवार संख्या'),
        ('children_population', 'बालबालिकाको जनसंख्या'),
        ('other_families', 'अन्य वर्गको परिवार संख्या'),
    ]

    program_detail = models.ForeignKey(ProgramDetail, on_delete=models.CASCADE, related_name='beneficiaries')
    title = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    female = models.PositiveIntegerField(null=True, blank=True, default=0)
    male = models.PositiveIntegerField(null=True, blank=True, default=0)
    other = models.PositiveIntegerField(null=True, blank=True, default=0)
    total = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.total = (self.female or 0) + (self.male or 0) + (self.other or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_title_display()} (Total: {self.total})"
