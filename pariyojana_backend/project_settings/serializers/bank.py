from rest_framework import serializers
from project_settings.models.bank import Bank

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
