from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.source import Source
from planning.PlanEntry.models import PlanEntry

class WardLevelProject(models.Model):
    plan_name = models.CharField(max_length=255)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward_no = models.TextField()
    status = models.CharField(max_length=255, default="प्रविष्टी भएको वडा स्तरीय परियोजना")
    priority_no = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.plan_name
    
    
    
    
    def save(self, *args, **kwargs):
        if not self.priority_no and not self.pk: 
            max_priority = WardLevelProject.objects.filter(
                ward_no=self.ward_no,
                is_deleted=False
            ).aggregate(models.Max('priority_no'))['priority_no__max'] or 0
            self.priority_no = max_priority + 1
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.plan_name
    
    






