from django.db import models
from projects.models.project import Project

SERIAL_CHOICES = (
    (1, "निर्माण कार्य गर्नु पुर्वको फोटोहरु"),
    (2, "योजनाको निर्माण कार्य भैरहेको अवस्थाको फोटोहरु"),
    (3, "योजनाको निर्माण कार्य सकिएपछीका फोटोहरु"),
)

def upload_to_operation_site(instance, filename):
    return f"operation_site_photos/project_{instance.project.serial_number}/{filename}"

class OperationSitePhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='operation_site_photos')

    serial_no = models.IntegerField(choices=SERIAL_CHOICES)
    title = models.CharField(max_length=255, blank=True)
    
    photo = models.ImageField(upload_to=upload_to_operation_site,null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.title = dict(SERIAL_CHOICES).get(self.serial_no, "")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project} - {self.get_serial_no_display()}"
