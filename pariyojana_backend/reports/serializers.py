from rest_framework import serializers
from project_settings.serializers.thematic_area import ThematicAreaSerializer
from project_settings.serializers.sub_thematic_area import SubAreaSerializer
from project_settings.serializers.source import SourceSerializer
from project_settings.serializers.expenditure_center import ExpenditureCenterSerializer
from project_settings.serializers.fiscal_year import FiscalYearSerializer


class ReportsDropdownsSerializer(serializers.Serializer):
    report_types = serializers.ListField(child=serializers.CharField())
    statuses = serializers.ListField(child=serializers.CharField())
    wards = serializers.ListField(child=serializers.CharField())

    thematic_areas = ThematicAreaSerializer(many=True)
    sub_areas = SubAreaSerializer(many=True)
    sources = SourceSerializer(many=True)
    expenditure_centers = ExpenditureCenterSerializer(many=True)
    fiscal_years = FiscalYearSerializer(many=True)
