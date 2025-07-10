
# models.py
from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.source import Source

class BudgetProgramMunicipalityPrideProgram(models.Model):
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = models.TextField()
    status = models.CharField(max_length=255, default="बजेट तथा कार्यक्रम तर्जुमा समितिमा सिफारिस भएको नगर गौरव आयोजना")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.plan_name
