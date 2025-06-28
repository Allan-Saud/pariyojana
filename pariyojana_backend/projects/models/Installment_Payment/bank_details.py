from django.db import models
from project_settings.models.bank import Bank
from projects.models.Consumer_Committee.official_detail import OfficialDetail  
from projects.models.project import Project
class BankDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bank_details', verbose_name="आयोजनाको नाम", null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name="बैंकको नाम")
    branch = models.CharField(max_length=255, verbose_name="बैंकको साखा")
    signatories = models.ManyToManyField(OfficialDetail, verbose_name="दस्तखत कर्ता", related_name="bank_signatories")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bank.name} - {self.branch}"
