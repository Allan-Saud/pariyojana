from rest_framework import serializers
from planning.MunicipalityPrideProject.SubmittedProjectsToBudgetCommittee.models import SubmittedToBudgetMunicipalityPrideProject
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from planning.PlanEntry.serializers import PlanEntrySerializer

class SimpleIdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class SubmittedToBudgetMunicipalityPrideProjectSerializer(serializers.ModelSerializer):
    plan_entry = PlanEntrySerializer(read_only=True)
    plan_entry_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanEntrySerializer.Meta.model.objects.all(),
        source='plan_entry',
        write_only=True,
        allow_null=True,
        required=False
    )

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

    # Include all other model fields as is
    class Meta:
        model = SubmittedToBudgetMunicipalityPrideProject
        fields = [
            'id',
            'plan_entry', 'plan_entry_id',
            'plan_name',
            'thematic_area', 'thematic_area_id',
            'sub_area', 'sub_area_id',
            'source', 'source_id',
            'expenditure_center', 'expenditure_center_id',
            'budget',
            'ward_no',
            'gps_coordinate',
            'expected_result',
            'location',
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
            'priority_no': {'required': False, 'allow_null': True},
            'plan_entry_id': {'required': False, 'allow_null': True},
        }
