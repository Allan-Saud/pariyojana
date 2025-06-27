from django.db import models
from django.core.exceptions import ValidationError
from projects.models.project import Project  # Adjust import if needed
from projects.models.cost_estimate_detail import CostEstimateDetail  # Adjust import if needed

class ProjectAgreementDetails(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='agreement_details')

    # Fields from CostEstimateDetail - fetched, read-only here, saved for record
    cost_estimate = models.DecimalField("लागत अनुमान", max_digits=15, decimal_places=2, null=True, blank=True)
    contingency_amount = models.DecimalField("कन्टिन्जेन्सि रकम", max_digits=15, decimal_places=2, null=True, blank=True)
    contingency_percentage = models.DecimalField("कन्टिन्जेन्सि प्रतिशत", max_digits=5, decimal_places=2, null=True, blank=True)
    total_cost_estimate = models.DecimalField("कुल लागत अनुमान", max_digits=15, decimal_places=2, null=True, blank=True)

    # User input fields
    agreement_amount = models.DecimalField("सम्झौता रकम रु.", max_digits=15, decimal_places=2)
    agreement_date = models.DateField("सम्झौता मिति")

    municipality_amount = models.DecimalField("नगरपालिकाले ब्यहेर्ने रकम", max_digits=15, decimal_places=2)
    municipality_percentage = models.DecimalField("नगरपालिकाले ब्यहेर्ने रकमको प्रतिशत (%)", max_digits=5, decimal_places=2, blank=True)

    public_participation_amount = models.DecimalField("जनसहभागिता", max_digits=15, decimal_places=2, blank=True)
    public_participation_percentage = models.DecimalField("जनसहभागिताले ब्यहेर्ने रकमको प्रतिशत (%)", max_digits=5, decimal_places=2, blank=True)

    work_order_date = models.DateField("कार्यादेश मिति")
    completion_date = models.DateField("कार्य सम्पन्न गर्नुपर्ने मिति")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Validation Rules
        if self.total_cost_estimate and self.agreement_amount > self.total_cost_estimate:
            raise ValidationError({'agreement_amount': 'सम्झौता रकम cannot be greater than कुल लागत अनुमान'})

        if self.municipality_amount > self.agreement_amount:
            raise ValidationError({'municipality_amount': 'नगरपालिकाले ब्यहेर्ने रकम cannot be greater than सम्झौता रकम'})

    def save(self, *args, **kwargs):
        # Fetch cost estimate data from CostEstimateDetail linked to this project
        try:
            cost_estimate_obj = CostEstimateDetail.objects.get(project=self.project)
            self.cost_estimate = cost_estimate_obj.estimated_cost
            self.contingency_amount = cost_estimate_obj.contingency_amount
            self.contingency_percentage = cost_estimate_obj.contingency_percent
            self.total_cost_estimate = cost_estimate_obj.total_estimated_cost
        except CostEstimateDetail.DoesNotExist:
            pass  # Or set defaults

        # Run validation
        self.clean()

        # Calculate percentages and participation amount automatically
        if self.agreement_amount > 0:
            self.municipality_percentage = round((self.municipality_amount / self.agreement_amount) * 100, 2)
            self.public_participation_amount = self.agreement_amount - self.municipality_amount
            self.public_participation_percentage = round(100 - self.municipality_percentage, 2)
        else:
            self.municipality_percentage = 0
            self.public_participation_amount = 0
            self.public_participation_percentage = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Agreement Details for Project {self.project.id}"
