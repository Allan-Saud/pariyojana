from rest_framework import serializers
from project_settings.models.sub_thematic_area import SubArea

class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'
