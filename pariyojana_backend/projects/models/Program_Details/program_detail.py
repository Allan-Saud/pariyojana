from django.db import models
from projects.models.project import Project
from django.db import models

class ProgramDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)  # link to Project
    project_name = models.CharField(max_length=255, blank=True)
    
    WARD_CHOICES = [(i, f'वडा नं {i}') for i in range(1, 9)]
    ward_no = models.PositiveIntegerField(choices=WARD_CHOICES, default=1)

    fiscal_year = models.ForeignKey('project_settings.FiscalYear', on_delete=models.SET_NULL, null=True, blank=True)
    area = models.ForeignKey('project_settings.ThematicArea', on_delete=models.SET_NULL, null=True, blank=True)
    sub_area = models.ForeignKey('project_settings.SubArea', on_delete=models.SET_NULL, null=True, blank=True)
    source = models.ForeignKey('project_settings.Source', on_delete=models.SET_NULL, null=True, blank=True)
    expenditure_center = models.ForeignKey('project_settings.ExpenditureCenter', on_delete=models.SET_NULL, null=True, blank=True)

    outcome = models.TextField("सम्पन्‍न गर्ने परिणाम", blank=True, null=True)
    budget = models.DecimalField("बजेट", max_digits=15, decimal_places=2, null=True, blank=True)
    location_gps = models.CharField("योजना संचालन स्थानको GPS CO-ORDINATE", max_length=255, blank=True, null=True)

    STATUS_CHOICES = [
        ('process_ensured', 'सुचारु प्रक्रिया सुनिस्चित भएको'),
        ('completed', 'सम्पन्न भएको'),
        ('not_started', 'सुरु नभएको'),
    ]
    status = models.CharField("स्थिती", max_length=20, choices=STATUS_CHOICES, default='not_started')

    project_level = models.ForeignKey('project_settings.ProjectLevel', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Program Detail for {self.project_name}"



