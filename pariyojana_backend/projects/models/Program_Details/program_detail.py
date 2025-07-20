from django.db import models
from projects.models.project import Project
from projects.models.Cost_Estimate.cost_estimate_detail import CostEstimateDetail
from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails  

class ProgramDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)


    @property
    def estimated_cost(self):
        try:
            return self.project.cost_estimate.estimated_cost
        except AttributeError:
            return None

    @property
    def contingency_amount(self):
        try:
            return self.project.cost_estimate.contingency_amount
        except AttributeError:
            return None

    @property
    def agreement_date(self):
        try:
            return self.project.agreement_details.agreement_date
        except AttributeError:
            return None

    @property
    def start_date(self):
        try:
            return self.project.agreement_details.work_order_date
        except AttributeError:
            return None

    @property
    def completion_date(self):
        try:
            return self.project.agreement_details.latest_completion_date or self.project.agreement_details.completion_date
        except AttributeError:
            return None

    @property
    def agreement_amount(self):
        try:
            return self.project.agreement_details.agreement_amount
        except AttributeError:
            return None

    @property
    def public_participation_amount(self):
        try:
            return self.project.agreement_details.public_participation_amount
        except AttributeError:
            return None
