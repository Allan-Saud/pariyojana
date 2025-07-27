from django.db import models, transaction
from django.db.models import Max
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
    YES_NO_CHOICES = [
        ('भएको', 'भएको'),
        ('नभएको', 'नभएको')
    ]

    plan_entry = models.ForeignKey(PlanEntry, on_delete=models.CASCADE, related_name="municipality_projects", null=True, blank=True)

    # ✅ Same fields as PlanEntry
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, null=True, blank=True)
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    project_level = models.ForeignKey(ProjectLevel, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_title = models.ForeignKey(ExpenditureTitle, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)

    # ✅ Additional fields
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = models.TextField(blank=True, null=True)
    gps_coordinate = models.CharField(max_length=255, blank=True, null=True)
    expected_result = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True)

    # ✅ Feasibility and studies
    feasibility_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    feasibility_file = models.FileField(upload_to="plan/feasibility/", null=True, blank=True)
    detailed_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    detailed_file = models.FileField(upload_to="plan/detailed/", null=True, blank=True)
    environmental_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    environmental_file = models.FileField(upload_to="plan/environmental/", null=True, blank=True)

    # ✅ Other fields
    status = models.CharField(max_length=255, default="प्रविष्टी भएको नगर स्तरीय परियोजना")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def _next_priority(self):
        """
        Get the next priority number among only active (not deleted) projects.
        """
        max_priority = MunicipalityLevelProject.objects.filter(is_deleted=False).aggregate(Max('priority_no'))['priority_no__max']
        return (max_priority or 0) + 1

    def save(self, *args, **kwargs):
        with transaction.atomic():  # Ensures no race condition
            if not self.priority_no:  # Only set if it's not manually assigned
                self.priority_no = self._next_priority()
            super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['priority_no'],
                condition=models.Q(is_deleted=False),
                name='unique_active_priority_municipality'
            )
        ]

    def __str__(self):
        return self.plan_name
