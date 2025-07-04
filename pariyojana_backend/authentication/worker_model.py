from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100)  # e.g., Department Chief, Engineer, etc.
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.designation})"
