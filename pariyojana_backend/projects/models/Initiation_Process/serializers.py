from rest_framework import serializers
from projects.models.Initiation_Process.initiation_process import InitiationProcess

class InitiationProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitiationProcess
        fields = '__all__'
        read_only_fields = ['project']
