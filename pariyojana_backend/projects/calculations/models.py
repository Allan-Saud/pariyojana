from django.db import models
from decimal import Decimal
from projects.models.project import Project
from project_settings.models.fiscal_year import FiscalYear

class CostEstimationCalculation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='cost_estimates')
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE, related_name='cost_estimates')

    provincial_budget = models.DecimalField(max_digits=12, decimal_places=2)
    local_budget = models.DecimalField(max_digits=12, decimal_places=2)

    total_without_vat = models.DecimalField(max_digits=12, decimal_places=2)
    ps_amount = models.DecimalField(max_digits=12, decimal_places=2)

    vat_percent = models.DecimalField(default=Decimal('13.00'), max_digits=5, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    contingency_percent = models.DecimalField(default=Decimal('3.00'), max_digits=5, decimal_places=2)
    contingency_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.vat_amount = (self.total_without_vat * self.vat_percent) / Decimal('100')
        self.contingency_amount = (self.total_without_vat * self.contingency_percent) / Decimal('100')
        self.grand_total = (
            self.total_without_vat +
            self.vat_amount +
            self.contingency_amount +
            self.ps_amount
        )
        super().save(*args, **kwargs)
