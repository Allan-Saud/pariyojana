from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.source import Source
from project_settings.models.project_level import ProjectLevel
from project_settings.models.unit import Unit
from project_settings.models.fiscal_year import FiscalYear
from project_settings.models.expenditure_title import ExpenditureTitle
from planning.PlanEntry.models import PlanEntry

class MunicipalityLevelProject(models.Model):
    plan_entry = models.ForeignKey(PlanEntry, on_delete=models.CASCADE, related_name="municipality_projects", null=True,blank=True)
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = models.TextField()
    status = models.CharField(max_length=255, default="प्रविष्टी भएको नगर स्तरीय परियोजना")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.plan_name
