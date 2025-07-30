from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.unit import Unit
from project_settings.models.fiscal_year import FiscalYear
from project_settings.models.project_level import ProjectLevel
from django.contrib.auth import get_user_model
from django.utils import timezone
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from django.contrib.postgres.fields import ArrayField
User = get_user_model()

class Project(models.Model):
    serial_number = models.AutoField(primary_key=True)  
    project_name = models.CharField("योजना तथा कार्यक्रम", max_length=255)
    area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT, verbose_name="क्षेत्र")
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT, verbose_name="उप-क्षेत्र")
    source = models.ForeignKey(Source, on_delete=models.PROTECT, verbose_name="स्रोत")
    expenditure_center = models.ForeignKey(ExpenditureCenter, on_delete=models.PROTECT, verbose_name="खर्च केन्द्र")
    project_level = models.ForeignKey(ProjectLevel, on_delete=models.SET_NULL, null=True, blank=True)
    budget = models.DecimalField("बजेट", max_digits=15, decimal_places=2)

    WARD_CHOICES = [(i, f"वडा नंं. {i}") for i in range(1, 9)]
    
    ward_no = ArrayField(
        models.IntegerField(choices=WARD_CHOICES),
        verbose_name="वडा नंं.",
        blank=True,
        default=list
    )

    STATUS_CHOICES = [
        ('process_ensured', 'सुचारु प्रक्रिया सुनिस्चित भएको'),
        ('completed', 'सम्पन्न भएको'),
        ('not_started', 'सुरु नभएको'),
    ]
    status = models.CharField("स्थिती", max_length=20, choices=STATUS_CHOICES, default='not_started',null=True,blank=True)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, verbose_name="आर्थिक वर्ष")

    location = models.CharField("योजना संचालन स्थान", max_length=255, null=True)

    location_gps = models.CharField("GPS CO-ORDINATE", max_length=100, null=True)
    outcome = models.TextField("सम्पन गर्ने परिणाम", null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, verbose_name="ईकाइ",null=True)

    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='deleted_projects')

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return f"{self.project_name} ({self.serial_number})"
    
    
    
    
    def are_all_documents_approved(self):
        """Check if all documents are approved for this project"""
        documents = self.map_cost_estimates.all()
        if not documents.exists():
            return False
            
        required_titles = [choice[0] for choice in MapCostEstimate.DOCUMENT_CHOICES]
        existing_titles = [doc.title for doc in documents]
        
        # Check all required documents are present
        if not all(title in existing_titles for title in required_titles):
            return False
            
        # Check all documents are approved
        return all(doc.status == 'approved' for doc in documents)