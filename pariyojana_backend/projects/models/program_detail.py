# from django.db import models
# from projects.models.project import Project


# class ProgramDetail(models.Model):
#     project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="program_detail")

#     # Snapshot fields from Project model
#     project_name = models.CharField(max_length=255, blank=True)
#     WARD_CHOICES = [(i, f'वडा नं {i}') for i in range(1, 9)]
#     ward_no = models.PositiveIntegerField(choices=WARD_CHOICES, default=1)
#     fiscal_year = models.ForeignKey('project_settings.FiscalYear', on_delete=models.SET_NULL, null=True, blank=True)
#     area = models.ForeignKey('project_settings.ThematicArea', on_delete=models.SET_NULL, null=True, blank=True)
#     sub_area = models.ForeignKey('project_settings.SubArea', on_delete=models.SET_NULL, null=True, blank=True)
#     source = models.ForeignKey('project_settings.Source', on_delete=models.SET_NULL, null=True, blank=True)
#     expenditure_center = models.ForeignKey('project_settings.ExpenditureCenter', on_delete=models.SET_NULL, null=True, blank=True)

#     # Other fields
#     location = models.CharField(max_length=255, blank=True, null=True)
#     project_level = models.CharField(max_length=255, blank=True, null=True)
#     allocated_budget = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     expected_output = models.PositiveIntegerField(default=0)
#     gps_coordinate = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=50, blank=True, null=True)

#     # From subcomponents
#     start_date = models.DateField(null=True, blank=True)
#     agreement_date = models.DateField(null=True, blank=True)
#     completion_date = models.DateField(null=True, blank=True)
#     economic_progress = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     physical_progress = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     estimated_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     contingency_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     agreement_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     consumer_contribution = models.DecimalField(max_digits=15, decimal_places=2, default=0)

#     def __str__(self):
#         return f"Program Detail for {self.project.project_name}"


# class BeneficiaryDetail(models.Model):
#     program_detail = models.ForeignKey(ProgramDetail, on_delete=models.CASCADE, related_name='beneficiaries')
#     title = models.CharField(max_length=255)
#     female = models.PositiveIntegerField(default=0)
#     male = models.PositiveIntegerField(default=0)
#     others = models.PositiveIntegerField(default=0)

#     @property
#     def total(self):
#         return self.female + self.male + self.others

#     def __str__(self):
#         return self.title
