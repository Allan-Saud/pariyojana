from rest_framework import serializers
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.thematic_area import ThematicArea

class ThematicAreaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = ['id', 'name']

class SubAreaSerializer(serializers.ModelSerializer):
    thematic_area = serializers.PrimaryKeyRelatedField(queryset=ThematicArea.objects.all())
    thematic_area_name = serializers.SerializerMethodField()

    class Meta:
        model = SubArea
        fields = '__all__'

    def get_thematic_area_name(self, obj):
        return obj.thematic_area.name if obj.thematic_area else None
