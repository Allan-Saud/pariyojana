# projects/models/cost_estimate_detail.py

from django.db import models

class CostEstimateDetail(models.Model):
    project = models.OneToOneField(
        'projects.Project', on_delete=models.CASCADE, related_name='cost_estimate'
    )

    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    contingency_percent = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)
    allocated_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    contingency_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False, default=0.00)
    total_estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, editable=False, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_fields(self):
        self.contingency_amount = round((self.estimated_cost * self.contingency_percent) / 100, 2)
        self.total_estimated_cost = round(self.estimated_cost + self.contingency_amount, 2)

    def save(self, *args, **kwargs):
        self.calculate_fields()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cost Estimate for Project {self.project_id}"
