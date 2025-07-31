from rest_framework import serializers
from .models import BudgetProgramMunicipalityPrideProgram
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.project_level import ProjectLevel
from project_settings.models.unit import Unit
from project_settings.models.expenditure_title import ExpenditureTitle
from project_settings.models.fiscal_year import FiscalYear
from planning.PlanEntry.serializers import PlanEntrySerializer


class SimpleIdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class BudgetProgramMunicipalityPrideProgramSerializer(serializers.ModelSerializer):
    # Plan Entry
    plan_entry = PlanEntrySerializer(read_only=True)
    plan_entry_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanEntrySerializer.Meta.model.objects.all(),
        source='plan_entry',
        write_only=True,
        allow_null=True,
        required=False
    )

    # Fiscal Year
    fiscal_year = serializers.SerializerMethodField()
    fiscal_year_id = serializers.PrimaryKeyRelatedField(
        queryset=FiscalYear.objects.all(),
        source='fiscal_year',
        write_only=True,
        allow_null=True,
        required=False
    )
    def get_fiscal_year(self, obj):
        return {"id": obj.fiscal_year.id, "name": str(obj.fiscal_year)} if obj.fiscal_year else None

    # Related fields (read: id+name, write: id only)
    thematic_area = SimpleIdNameSerializer(read_only=True)
    thematic_area_id = serializers.PrimaryKeyRelatedField(
        queryset=ThematicArea.objects.all(), source='thematic_area', write_only=True
    )

    sub_area = SimpleIdNameSerializer(read_only=True)
    sub_area_id = serializers.PrimaryKeyRelatedField(
        queryset=SubArea.objects.all(), source='sub_area', write_only=True
    )

    project_level = SimpleIdNameSerializer(read_only=True)
    project_level_id = serializers.PrimaryKeyRelatedField(
        queryset=ProjectLevel.objects.all(), source='project_level',
        write_only=True, allow_null=True, required=False
    )

    expenditure_title = SimpleIdNameSerializer(read_only=True)
    expenditure_title_id = serializers.PrimaryKeyRelatedField(
        queryset=ExpenditureTitle.objects.all(), source='expenditure_title',
        write_only=True, allow_null=True, required=False
    )

    expenditure_center = SimpleIdNameSerializer(read_only=True)
    expenditure_center_id = serializers.PrimaryKeyRelatedField(
        queryset=ExpenditureCenter.objects.all(), source='expenditure_center', write_only=True
    )

    source = SimpleIdNameSerializer(read_only=True)
    source_id = serializers.PrimaryKeyRelatedField(
        queryset=Source.objects.all(), source='source', write_only=True
    )

    unit = SimpleIdNameSerializer(read_only=True)
    unit_id = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all(), source='unit', write_only=True,
        allow_null=True, required=False
    )

    class Meta:
        model = BudgetProgramMunicipalityPrideProgram
        fields = [
            'id',
            'plan_entry', 'plan_entry_id',
            'fiscal_year', 'fiscal_year_id',
            'plan_name',
            'thematic_area', 'thematic_area_id',
            'sub_area', 'sub_area_id',
            'project_level', 'project_level_id',
            'expenditure_title', 'expenditure_title_id',
            'expenditure_center', 'expenditure_center_id',
            'source', 'source_id',
            'unit', 'unit_id',
            'budget',
            'ward_no',
            'gps_coordinate',
            'expected_result',
            'location',
            'feasibility_study', 'feasibility_file',
            'detailed_study', 'detailed_file',
            'environmental_study', 'environmental_file',
            'status',
            'priority_no',
            'remarks',
            'is_deleted',
            'deleted_at',
        ]
        extra_kwargs = {
            'plan_entry_id': {'required': False},
            'fiscal_year_id': {'required': False},
            'project_level_id': {'required': False},
            'expenditure_title_id': {'required': False},
            'unit_id': {'required': False},
            'feasibility_file': {'required': False, 'allow_null': True},
            'detailed_file': {'required': False, 'allow_null': True},
            'environmental_file': {'required': False, 'allow_null': True},
        }
