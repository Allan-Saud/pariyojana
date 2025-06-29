from django.db import models
from projects.models.project import Project 
class ConsumerCommitteeDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='consumer_committees',null=True) 
    consumer_committee_name = models.CharField(max_length=255)
    address = models.TextField()
    formation_date = models.DateField()
    representative_name = models.CharField(max_length=255)
    representative_position = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
