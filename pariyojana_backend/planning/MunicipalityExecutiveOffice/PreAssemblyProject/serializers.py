from rest_framework import serializers
from .models import PreAssemblyProject

class PreAssemblyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAssemblyProject
        fields = '__all__'
