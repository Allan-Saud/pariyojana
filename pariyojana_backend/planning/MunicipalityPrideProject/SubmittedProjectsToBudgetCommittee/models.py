from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.source import Source
from planning.PlanEntry.models import PlanEntry
from django.contrib.postgres.fields import ArrayField
YES_NO_CHOICES = [
    ('भएको', 'भएको'),
    ('नभएको', 'नभएको')
]

class SubmittedToBudgetMunicipalityPrideProject(models.Model):
    plan_entry = models.ForeignKey(PlanEntry, on_delete=models.CASCADE, related_name="submitted_budget_projects", null=True, blank=True)

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

    gps_coordinate = models.CharField(max_length=255, blank=True, null=True)  # Optional
    expected_result = models.TextField(blank=True, null=True)  # Optional
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional

    feasibility_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    feasibility_file = models.FileField(upload_to="plan/feasibility/", null=True, blank=True)
    detailed_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    detailed_file = models.FileField(upload_to="plan/detailed/", null=True, blank=True)
    environmental_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    environmental_file = models.FileField(upload_to="plan/environmental/", null=True, blank=True)

    status = models.CharField(max_length=255, default="बजेट तथा कार्यक्रम तर्जुमा समितिमा पेश गरिएको परियोजना")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.plan_name
