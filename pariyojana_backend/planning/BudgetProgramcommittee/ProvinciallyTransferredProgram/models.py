from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.expenditure_title import ExpenditureTitle
from project_settings.models.unit import Unit
from project_settings.models.fiscal_year import FiscalYear
from project_settings.models.source import Source
from project_settings.models.project_level import ProjectLevel
from planning.PlanEntry.models import PlanEntry
from django.contrib.postgres.fields import ArrayField

YES_NO_CHOICES = [
    ('भएको', 'भएको'),
    ('नभएको', 'नभएको')
]

class ProvinciallytransferredProgram(models.Model):
    plan_entry = models.ForeignKey(PlanEntry, on_delete=models.CASCADE, related_name="province_projects", blank=True, null=True)

    # ✅ Include all fields from PlanEntry
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, null=True, blank=True)
    plan_name = models.CharField(max_length=255, verbose_name="योजना तथा कार्यक्रम")
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT, verbose_name="क्षेत्र")
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT, verbose_name="उप-क्षेत्र")
    project_level = models.ForeignKey(ProjectLevel, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_title = models.ForeignKey(ExpenditureTitle, on_delete=models.PROTECT, null=True, blank=True)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT, verbose_name="खर्च केन्द्र")
    source = models.ForeignKey(Source, on_delete=models.PROTECT, verbose_name="स्रोत")
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True)

    budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="बजेट")
    ward_no = ArrayField(
    base_field=models.IntegerField(),
    blank=True,
    default=list,
    verbose_name="वडा नं."
)
    gps_coordinate = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    expected_result = models.TextField(blank=True, null=True)

    # ✅ Study fields
    feasibility_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    feasibility_file = models.FileField(upload_to="plan/feasibility/", null=True, blank=True)
    detailed_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    detailed_file = models.FileField(upload_to="plan/detailed/", null=True, blank=True)
    environmental_study = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    environmental_file = models.FileField(upload_to="plan/environmental/", null=True, blank=True)

    # ✅ Other fields
    status = models.CharField(max_length=255, verbose_name="स्थिती", default="प्रदेश परियोजना अन्तर्गत प्रविष्टी भएको")
    priority_no = models.PositiveIntegerField(verbose_name="प्राथमिकता नम्बर", null=True, blank=True)
    remarks = models.TextField(verbose_name="अन्य", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.plan_name
