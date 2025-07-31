from rest_framework import serializers
from .models import ThematicCommitteeProgram
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.project_level import ProjectLevel
from project_settings.models.unit import Unit
from project_settings.models.expenditure_title import ExpenditureTitle
from project_settings.models.fiscal_year import FiscalYear
from planning.PlanEntry.models import PlanEntry


class SimpleIdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class FiscalYearSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    year = serializers.CharField()


class ThematicCommitteeProgramSerializer(serializers.ModelSerializer):
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

    project_level = SimpleIdNameSerializer(read_only=True, allow_null=True)
    project_level_id = serializers.PrimaryKeyRelatedField(
        queryset=ProjectLevel.objects.all(),
        source='project_level',
        write_only=True,
        allow_null=True,
        required=False
    )

    expenditure_title = SimpleIdNameSerializer(read_only=True, allow_null=True)
    expenditure_title_id = serializers.PrimaryKeyRelatedField(
        queryset=ExpenditureTitle.objects.all(),
        source='expenditure_title',
        write_only=True,
        allow_null=True,
        required=False
    )

    unit = SimpleIdNameSerializer(read_only=True, allow_null=True)
    unit_id = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all(),
        source='unit',
        write_only=True,
        allow_null=True,
        required=False
    )

    fiscal_year = FiscalYearSerializer(read_only=True, allow_null=True)
    fiscal_year_id = serializers.PrimaryKeyRelatedField(
        queryset=FiscalYear.objects.all(),
        source='fiscal_year',
        write_only=True,
        allow_null=True,
        required=False
    )

    plan_entry = serializers.PrimaryKeyRelatedField(
        queryset=PlanEntry.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = ThematicCommitteeProgram
        fields = [
            'id',
            'plan_name',
            'thematic_area', 'thematic_area_id',
            'sub_area', 'sub_area_id',
            'source', 'source_id',
            'expenditure_center', 'expenditure_center_id',
            'project_level', 'project_level_id',
            'expenditure_title', 'expenditure_title_id',
            'unit', 'unit_id',
            'fiscal_year', 'fiscal_year_id',
            'plan_entry',
            'budget',
            'ward_no',
            'status',
            'priority_no',
            'remarks',
            'created_at',
            'is_deleted',
            'deleted_at',
        ]
