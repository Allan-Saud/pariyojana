from rest_framework import serializers
from project_settings.models.template import Template

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'
