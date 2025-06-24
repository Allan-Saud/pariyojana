from django.db import models

class ThematicArea(models.Model):
    name = models.CharField(max_length=255)
    committee_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
