from rest_framework import serializers
from project_settings.models.group import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
