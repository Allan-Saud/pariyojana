from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.source import Source
from planning.PlanEntry.models import PlanEntry
from django.db import models, transaction
from django.db.models import Max
from django.utils import timezone

class MunicipalityPrideProject(models.Model):
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = models.TextField()
    status = models.CharField(max_length=255, default="प्रविष्टी भएको नगर गौरव आयोजना")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.plan_name
    
    
    
    def _next_priority(self):
        """
        Return the next integer after the current highest priority_no
        among *active* (not soft‑deleted) projects.
        """
        highest = (
            MunicipalityPrideProject.objects
            .filter(is_deleted=False)           # or .filter(is_deleted=False, ward_no=self.ward_no)
            .aggregate(Max('priority_no'))['priority_no__max']
        )
        return (highest or 0) + 1

    def save(self, *args, **kwargs):
        with transaction.atomic():             # prevents duplicate numbers under load
            if self.priority_no in (None, ''):
                self.priority_no = self._next_priority()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.plan_name

    class Meta:
        constraints = [
            # guarantees no two *active* projects share the same number
            models.UniqueConstraint(
                fields=['priority_no'],
                condition=models.Q(is_deleted=False),
                name='uniq_priority_active_prideproject',
            )
        ]
    






