from rest_framework import serializers
from planning.WardOffice.WardLevelProject.models import WardLevelProject

class WardLevelProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardLevelProject
        fields = '__all__'
