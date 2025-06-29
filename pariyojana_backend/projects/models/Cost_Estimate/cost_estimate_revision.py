from django.db import models
from django.contrib.auth import get_user_model
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail

User = get_user_model()

class CostEstimateRevision(models.Model):
    cost_estimate = models.ForeignKey(
        CostEstimateDetail,
        on_delete=models.CASCADE,
        related_name='revisions'
    )

    # Previous values 
    prev_estimated_cost = models.DecimalField(max_digits=12, decimal_places=2)
    prev_contingency_percent = models.DecimalField(max_digits=5, decimal_places=2)
    prev_contingency_amount = models.DecimalField(max_digits=12, decimal_places=2)
    prev_total_estimated_cost = models.DecimalField(max_digits=12, decimal_places=2)

    # Revised inputs
    revised_estimated_cost = models.DecimalField(max_digits=12, decimal_places=2)
    revised_contingency_percent = models.DecimalField(max_digits=5, decimal_places=2)
    revised_contingency_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    revised_total_estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    revised_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def calculate_revised_fields(self):
        self.revised_contingency_amount = round((self.revised_estimated_cost * self.revised_contingency_percent) / 100, 2)
        self.revised_total_estimated_cost = round(self.revised_estimated_cost + self.revised_contingency_amount, 2)

    def save(self, *args, **kwargs):
        # Store previous snapshot
        if not self.pk:
            self.prev_estimated_cost = self.cost_estimate.estimated_cost
            self.prev_contingency_percent = self.cost_estimate.contingency_percent
            self.prev_contingency_amount = self.cost_estimate.contingency_amount
            self.prev_total_estimated_cost = self.cost_estimate.total_estimated_cost

        # Calculate revised values
        self.calculate_revised_fields()

        # Update the main CostEstimateDetail
        self.cost_estimate.estimated_cost = self.revised_estimated_cost
        self.cost_estimate.contingency_percent = self.revised_contingency_percent
        self.cost_estimate.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Revision for Project {self.cost_estimate.project_id} at {self.created_at}"
