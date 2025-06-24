from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Project(TimestampedModel):
    serial = models.CharField(max_length=50)                # क्र.स 
    name = models.CharField(max_length=255)                 # योजना तथा कार्यक्रम
    sector = models.CharField(max_length=255)               # क्षेत्र
    sub_sector = models.CharField(max_length=255, blank=True, null=True)  # उप-क्षेत्र
    source = models.CharField(max_length=255)               # स्रोत
    cost_center = models.CharField(max_length=255)          # खर्च केन्द्र
    budget = models.DecimalField(max_digits=15, decimal_places=2)       # बजेट
    ward_no = models.CharField(max_length=10)               # वडा नंं.
    status = models.CharField(max_length=100)               # स्थिती

    def __str__(self):
        return self.name

class ProjectDetail(TimestampedModel):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='detail')
    program_detail = models.TextField(blank=True)           # कार्यक्रमको विवरण
    implementation_process = models.TextField(blank=True)   # सुचारु प्रक्रिया
    consumer_committee = models.TextField(blank=True)       # उपभोक्ता समिति
    cost_estimate = models.TextField(blank=True)            # लागत अनुमान
    agreement = models.TextField(blank=True)                # योजना सम्झौता
    operation_site = models.TextField(blank=True)           # सञ्चालन स्थल
    installment_payment = models.TextField(blank=True)      # किस्ता भुक्तानी सम्बन्धी
    other_documents = models.TextField(blank=True)          # अन्य डकुमेन्ट

    def __str__(self):
        return f"Detail for {self.project}"
