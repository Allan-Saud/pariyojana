# models/supplier_registry.py
from django.db import models

class SupplierRegistry(models.Model):
    fiscal_year = models.CharField(max_length=10)  # आर्थिक वर्ष

    # Section 1: Supplier Info
    company_name = models.CharField(max_length=255)  # कम्पनीको नाम
    address = models.CharField(max_length=255)
    correspondence_address = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    company_registration_number = models.CharField(max_length=50)
    pan_number = models.CharField(max_length=50)

    # Section 2: Document Checkboxes (Yes/No)
    has_registration_certificate = models.BooleanField()  # संस्था वा फर्म दर्ताको प्रमाणपत्र
    is_renewed = models.BooleanField()                    # नविकरण गरिएको
    has_vat_pan_certificate = models.BooleanField()       # मूल्य अभिवृद्धि कर वा प्यान
    has_tax_clearance = models.BooleanField()             # कर चुक्ता प्रमाणपत्र
    has_license_copy = models.BooleanField()              # इजाजत पत्र

    # Section 3: Nature of Procurement (comments/text)
    goods_description = models.TextField(blank=True, null=True)  # मालसामान
    construction_description = models.TextField(blank=True, null=True)
    consulting_description = models.TextField(blank=True, null=True)
    other_services_description = models.TextField(blank=True, null=True)

    # File uploads (optional)
    registration_certificate_file = models.FileField(upload_to='supplier_docs/', null=True, blank=True)
    license_file = models.FileField(upload_to='supplier_docs/', null=True, blank=True)
    tax_clearance_file = models.FileField(upload_to='supplier_docs/', null=True, blank=True)
    pan_file = models.FileField(upload_to='supplier_docs/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

