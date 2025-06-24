from rest_framework import viewsets
from project_settings.models.template import Template
from project_settings.serializers.template import TemplateSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
