from rest_framework import serializers
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter

class SimpleIdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class CouncilSubmittedProjectsSerializer(serializers.ModelSerializer):
    thematic_area = SimpleIdNameSerializer(read_only=True)
    thematic_area_id = serializers.PrimaryKeyRelatedField(
        queryset=ThematicArea.objects.all(),
        source='thematic_area',
        write_only=True
    )

    sub_area = SimpleIdNameSerializer(read_only=True)
    sub_area_id = serializers.PrimaryKeyRelatedField(
        queryset=SubArea.objects.all(),
        source='sub_area',
        write_only=True
    )

    source = SimpleIdNameSerializer(read_only=True)
    source_id = serializers.PrimaryKeyRelatedField(
        queryset=Source.objects.all(),
        source='source',
        write_only=True
    )

    expenditure_center = SimpleIdNameSerializer(read_only=True)
    expenditure_center_id = serializers.PrimaryKeyRelatedField(
        queryset=ExpenditureCenter.objects.all(),
        source='expenditure_center',
        write_only=True
    )

    # Include all other model fields directly
    plan_name = serializers.CharField()
    budget = serializers.DecimalField(max_digits=15, decimal_places=2)
    ward_no = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    
    feasibility_study = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    feasibility_file = serializers.FileField(allow_null=True, required=False)
    detailed_study = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    detailed_file = serializers.FileField(allow_null=True, required=False)
    environmental_study = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    environmental_file = serializers.FileField(allow_null=True, required=False)
    
    status = serializers.CharField()
    priority_no = serializers.IntegerField(allow_null=True, required=False)
    remarks = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    is_deleted = serializers.BooleanField()
    deleted_at = serializers.DateTimeField(allow_null=True, required=False)

    class Meta:
        model = CouncilSubmittedProject
        fields = [
            'id',
            'plan_name',
            'thematic_area', 'thematic_area_id',
            'sub_area', 'sub_area_id',
            'source', 'source_id',
            'expenditure_center', 'expenditure_center_id',
            'budget',
            'ward_no',
            'feasibility_study',
            'feasibility_file',
            'detailed_study',
            'detailed_file',
            'environmental_study',
            'environmental_file',
            'status',
            'priority_no',
            'remarks',
            'is_deleted',
            'deleted_at',
        ]
        extra_kwargs = {
            'feasibility_file': {'required': False, 'allow_null': True},
            'detailed_file': {'required': False, 'allow_null': True},
            'environmental_file': {'required': False, 'allow_null': True},
            'priority_no': {'required': False},
        }
