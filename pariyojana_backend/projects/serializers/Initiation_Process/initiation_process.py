# projects/serializers/initiation_process.py

from rest_framework import serializers
from projects.models.Initiation_Process.initiation_process import InitiationProcess

class InitiationProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitiationProcess
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.initiation_method = validated_data.get('initiation_method', instance.initiation_method)
        instance.is_confirmed = validated_data.get('is_confirmed', instance.is_confirmed)

        if instance.is_confirmed:
            instance.initiate_project()

        instance.save()
        return instance
