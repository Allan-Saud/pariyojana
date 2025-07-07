from rest_framework import serializers
from projects.models.project import Project

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'
#         read_only_fields = ['id', 'created_at', 'updated_at', 'deleted_at', 'deleted_by', 'is_deleted']

class ProjectSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source='area.name', read_only=True)
    sub_area_name = serializers.CharField(source='sub_area.name', read_only=True)
    source_name = serializers.CharField(source='source.name', read_only=True)
    expenditure_center_name = serializers.CharField(source='expenditure_center.name', read_only=True)
    fiscal_year_name = serializers.CharField(source='fiscal_year.year', read_only=True)
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    project_level_name = serializers.CharField(source='project_level.name', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'deleted_at', 'deleted_by', 'is_deleted']
