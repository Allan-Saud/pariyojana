from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from django.contrib.postgres.fields import ArrayField
class ProjectsApprovedByMunicipal(models.Model):
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = ArrayField(
    base_field=models.IntegerField(),
    blank=True,
    default=list,
    verbose_name="वडा नं."
)
    status = models.CharField(max_length=255, default="सभाद्वारा स्वीकृत भएको")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)  # अन्य: editable

    def __str__(self):
        return self.plan_name
