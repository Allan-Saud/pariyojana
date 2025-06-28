from rest_framework import serializers
from authentication.worker_model import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
