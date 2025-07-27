from rest_framework import serializers
from planning.WardOffice.WardLevelProject.models import WardLevelProject
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.unit import Unit
from project_settings.models.project_level import ProjectLevel

from project_settings.models.expenditure_center import ExpenditureCenter   
     

class WardLevelProjectSerializer(serializers.ModelSerializer):
    thematic_area = serializers.SlugRelatedField(slug_field='name', queryset=ThematicArea.objects.all())
    sub_area = serializers.SlugRelatedField(slug_field='name', queryset=SubArea.objects.all())
    source = serializers.SlugRelatedField(slug_field='name', queryset=Source.objects.all())
    unit = serializers.SlugRelatedField(slug_field='name', queryset=Unit.objects.all())
    project_level = serializers.SlugRelatedField(slug_field='name', queryset=ProjectLevel.objects.all())
    expenditure_center = serializers.SlugRelatedField(slug_field='name', queryset=ExpenditureCenter.objects.all())
    
    class Meta:
        model = WardLevelProject
        fields = '__all__'
        extra_kwargs = {
            'priority_no': {'required': False}
        }
        
        
# from rest_framework import serializers
# from .models import WardLevelProject
# from planning.PlanEntry.models import PlanEntry
# from planning.PlanEntry.serializers import PlanEntrySerializer  # 👈 import it

# class WardLevelProjectSerializer(serializers.ModelSerializer):
#     plan_entry = PlanEntrySerializer(read_only=True)  # 👈 nested serializer

#     class Meta:
#         model = WardLevelProject
#         fields = '__all__'

