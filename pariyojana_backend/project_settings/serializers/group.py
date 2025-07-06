from rest_framework import serializers
from project_settings.models.group import Group
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea

class ThematicAreaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = ['id', 'name']

class SubAreaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = ['id', 'name']

class GroupSerializer(serializers.ModelSerializer):
    thematic_area = serializers.PrimaryKeyRelatedField(queryset=ThematicArea.objects.all())
    sub_area = serializers.PrimaryKeyRelatedField(queryset=SubArea.objects.all())


    thematic_area_details = ThematicAreaSimpleSerializer(source='thematic_area', read_only=True)
    sub_area_details = SubAreaSimpleSerializer(source='sub_area', read_only=True)

    class Meta:
        model = Group
        fields = '__all__'
