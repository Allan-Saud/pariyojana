# projects/serializers/program_detail.py

from rest_framework import serializers
from projects.models.Program_Details.program_detail import ProgramDetail
from projects.models.project import Project

class ProgramDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDetail
        fields = '__all__'

    def create(self, validated_data):
        project = validated_data.get('project')

        if project:
            validated_data.setdefault('project_name', project.project_name)
            validated_data.setdefault('ward_no', project.ward_no)
            validated_data.setdefault('fiscal_year', project.fiscal_year)
            validated_data.setdefault('area', project.area)
            validated_data.setdefault('sub_area', project.sub_area)
            validated_data.setdefault('source', project.source)
            validated_data.setdefault('expenditure_center', project.expenditure_center)
            validated_data.setdefault('outcome', project.outcome)
            validated_data.setdefault('budget', project.budget)
            validated_data.setdefault('location_gps', project.location_gps)
            validated_data.setdefault('status', project.status)

        return super().create(validated_data)
