from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.expenditure_title import ExpenditureTitle
from project_settings.models.unit import Unit
from project_settings.models.fiscal_year import FiscalYear
from project_settings.models.source import Source
from project_settings.models.project_level import ProjectLevel
from django.conf import settings

PROJECT_TYPE_CHOICES = [
    ('ward_level', 'Ward-level Project'),
    ('municipality_level', 'Municipality-level Project'),
    ('ward_requested_thematic', 'Projects of Thematic Committees Requested by the Ward'),
    ('thematic_committee', 'Projects of Thematic Committees'),
    ('pride_project', 'Municipal Pride Project'),
    ('provincial', 'Provincial Government Project'),
    ('federal', 'Federal Government Project'),
]

YES_NO_CHOICES = [
    ('भएको', 'भएको'),
    ('नभएको', 'नभएको')
]

class PlanEntry(models.Model):
    plan_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT)
    plan_name = models.CharField(max_length=255)

    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    # project_level = models.ForeignKey(ProjectLevel, on_delete=models.PROTECT)
    expenditure_title = models.ForeignKey(ExpenditureTitle, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    project_level = models.ForeignKey(ProjectLevel, on_delete=models.PROTECT,null=True)
    proposed_amount = models.DecimalField(max_digits=15, decimal_places=2)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    ward_no = models.TextField(blank=True,null=True)
    gps_coordinate = models.CharField(max_length=255, blank=True, null=True)
    expected_result = models.TextField(blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True)

    # Feasibility-related fields
    feasibility_study = models.CharField(max_length=10, choices=YES_NO_CHOICES)
    feasibility_file = models.FileField(upload_to="plan/feasibility/", null=True, blank=True)

    detailed_study = models.CharField(max_length=10, choices=YES_NO_CHOICES)
    detailed_file = models.FileField(upload_to="plan/detailed/", null=True, blank=True)

    environmental_study = models.CharField(max_length=10, choices=YES_NO_CHOICES)
    environmental_file = models.FileField(upload_to="plan/environmental/", null=True, blank=True)

    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_plan_entries'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan_name
