from rest_framework import serializers
from planning.WardOffice.WardThematicCommitteeProjects.models import WardThematicCommitteeProject
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter   
from planning.PlanEntry.serializers import PlanEntrySerializer

class WardThematicCommitteeProjectSerializer(serializers.ModelSerializer):
    thematic_area = serializers.SlugRelatedField(slug_field='name', queryset=ThematicArea.objects.all())
    sub_area = serializers.SlugRelatedField(slug_field='name', queryset=SubArea.objects.all())
    source = serializers.SlugRelatedField(slug_field='name', queryset=Source.objects.all())
    expenditure_center = serializers.SlugRelatedField(slug_field='name', queryset=ExpenditureCenter.objects.all())
    plan_entry = PlanEntrySerializer(read_only=True)
    class Meta:
        model = WardThematicCommitteeProject
        fields = '__all__'
