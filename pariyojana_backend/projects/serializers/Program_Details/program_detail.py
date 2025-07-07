# # projects/serializers/program_detail.py

# from rest_framework import serializers
# from projects.models.Program_Details.program_detail import ProgramDetail
# from projects.models.project import Project

# class ProgramDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProgramDetail
#         fields = '__all__'

#     def create(self, validated_data):
#         project = validated_data.get('project')

#         if project:
#             validated_data.setdefault('project_name', project.project_name)
#             validated_data.setdefault('ward_no', project.ward_no)
#             validated_data.setdefault('fiscal_year', project.fiscal_year)
#             validated_data.setdefault('area', project.area)
#             validated_data.setdefault('sub_area', project.sub_area)
#             validated_data.setdefault('source', project.source)
#             validated_data.setdefault('expenditure_center', project.expenditure_center)
#             validated_data.setdefault('outcome', project.outcome)
#             validated_data.setdefault('budget', project.budget)
#             validated_data.setdefault('location_gps', project.location_gps)
#             validated_data.setdefault('status', project.status)

#         return super().create(validated_data)


from rest_framework import serializers
from projects.models.Program_Details.program_detail import ProgramDetail

class ProgramDetailSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.project_name', read_only=True)
    ward_no = serializers.IntegerField(source='project.ward_no', read_only=True)
    fiscal_year = serializers.CharField(source='project.fiscal_year.year_name', read_only=True)
    area = serializers.CharField(source='project.area.name', read_only=True)
    sub_area = serializers.CharField(source='project.sub_area.name', read_only=True)
    source = serializers.CharField(source='project.source.name', read_only=True)
    expenditure_center = serializers.CharField(source='project.expenditure_center.name', read_only=True)
    project_level = serializers.CharField(source='project.project_level.name', read_only=True)
    budget = serializers.DecimalField(source='project.budget', max_digits=15, decimal_places=2, read_only=True)

    class Meta:
        model = ProgramDetail
        fields = [
            'id', 'project_name', 'ward_no', 'fiscal_year', 'area', 'sub_area',
            'source', 'expenditure_center', 'project_level', 'budget',
            'outcome', 'location_gps', 'status', 'project_start_date'
        ]
