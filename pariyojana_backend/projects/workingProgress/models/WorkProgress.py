from django.db import models
from projects.models.project  import Project
from project_settings.models.fiscal_year import FiscalYear
from projects.workingProgress.models.WorkType   import WorkType


class WorkProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='work_progresses')
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)  
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'fiscal_year', 'work_type') 

    def __str__(self):
        return f"{self.project} - {self.work_type.name}: {self.quantity} {self.work_type.unit}"
