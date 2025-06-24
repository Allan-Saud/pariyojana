from django.db import models
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea


class Group(models.Model):
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.CASCADE)
    sub_area = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)