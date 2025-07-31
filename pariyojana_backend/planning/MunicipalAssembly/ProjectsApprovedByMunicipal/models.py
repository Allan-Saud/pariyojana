from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.unit import Unit
from project_settings.models.project_level import ProjectLevel
from project_settings.models.fiscal_year import FiscalYear
from project_settings.models.expenditure_title import ExpenditureTitle
from django.contrib.postgres.fields import ArrayField

YES_NO_CHOICES = [
    ('भएको', 'भएको'),
    ('नभएको', 'नभएको')
]

class ProjectsApprovedByMunicipal(models.Model):
    # Optional PlanEntry relation if needed in future
    # plan_entry = models.ForeignKey(PlanEntry, on_delete=models.CASCADE, related_name="approved_projects", null=True, blank=True)

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, null=True, blank=True)
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    project_level = models.ForeignKey(ProjectLevel, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_title = models.ForeignKey(ExpenditureTitle, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True)

    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = ArrayField(
        base_field=models.IntegerField(),
        blank=True,
        default=list,
        verbose_name="वडा नं."
    )

    gps_coordinate = models.CharField(max_length=255, blank=True, null=True)
    expected_result = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    feasibility_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    feasibility_file = models.FileField(upload_to="plan/feasibility/", null=True, blank=True)
    detailed_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    detailed_file = models.FileField(upload_to="plan/detailed/", null=True, blank=True)
    environmental_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    environmental_file = models.FileField(upload_to="plan/environmental/", null=True, blank=True)

    status = models.CharField(max_length=255, default="सभाद्वारा स्वीकृत भएको")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.plan_name
