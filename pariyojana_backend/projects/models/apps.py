# def ready(self):
#     import projects.signals  # assuming your signals are in projects/signals.py


# projects/apps.py
from django.apps import AppConfig

class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

    def ready(self):
        import projects.signals  # This line connects your signals