from rest_framework import serializers
from planning.WardOffice.PrioritizedWardLevelProjects.models import PrioritizedWardLevelProject
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter   
     

class PrioritizedWardLevelProjectSerializer(serializers.ModelSerializer):
    thematic_area = serializers.SlugRelatedField(slug_field='name', queryset=ThematicArea.objects.all())
    sub_area = serializers.SlugRelatedField(slug_field='name', queryset=SubArea.objects.all())
    source = serializers.SlugRelatedField(slug_field='name', queryset=Source.objects.all())
    expenditure_center = serializers.SlugRelatedField(slug_field='name', queryset=ExpenditureCenter.objects.all())
    class Meta:
        model = PrioritizedWardLevelProject
        fields = '__all__'
