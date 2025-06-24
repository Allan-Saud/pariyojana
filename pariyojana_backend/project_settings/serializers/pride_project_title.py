from rest_framework import serializers
from project_settings.models.pride_project_title import PrideProjectTitle

class PrideProjectTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrideProjectTitle
        fields = '__all__'
