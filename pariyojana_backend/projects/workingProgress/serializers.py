from rest_framework import serializers
from projects.workingProgress.models.WorkType import WorkType
from projects.workingProgress.models.WorkProgress import WorkProgress
  


class WorkTypeSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    class Meta:
        model = WorkType
        fields = ['id', 'project', 'name', 'unit','unit_name']
        read_only_fields = ['project'] 

# class WorkProgressSerializer(serializers.ModelSerializer):
#     work_type = WorkTypeSerializer(read_only=True)
#     work_type_id = serializers.PrimaryKeyRelatedField(queryset=WorkType.objects.all(), source='work_type', write_only=True)

#     project_name = serializers.CharField(source='project.project_name', read_only=True)
#     fiscal_year_display = serializers.CharField(source='fiscal_year.year', read_only=True)

#     class Meta:
#         model = WorkProgress
#         fields = ['id', 'project_name', 'fiscal_year', 'fiscal_year_display', 'work_type', 'quantity', 'remarks', 'created_at']
#         read_only_fields = ['created_at', 'project_name', 'fiscal_year_display', 'project', 'work_type_id']

class WorkProgressSerializer(serializers.ModelSerializer):
    work_type = WorkTypeSerializer(read_only=True)

    project_name = serializers.CharField(source='project.project_name', read_only=True)
    fiscal_year_display = serializers.CharField(source='fiscal_year.year', read_only=True)

    class Meta:
        model = WorkProgress
        fields = [
            'id',
            'project_name',
            'fiscal_year',
            'fiscal_year_display',
            'work_type',        # readable nested view
            'quantity',
            'remarks',
            'created_at'
        ]
        read_only_fields = [
            'created_at',
            'project_name',
            'fiscal_year_display',
            'project',
            'work_type'
        ]

