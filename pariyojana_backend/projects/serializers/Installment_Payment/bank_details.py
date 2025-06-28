from rest_framework import serializers
from projects.models.Installment_Payment.bank_details import BankDetail
from project_settings.models.bank import Bank
from projects.models.Consumer_Committee.official_detail import OfficialDetail

class OfficialDetailSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = OfficialDetail
        fields = ['id', 'full_name', 'post', 'display_name']

    def get_display_name(self, obj):
        return f"{obj.full_name} ({obj.post})"

class BankDetailSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    signatories_details = OfficialDetailSerializer(source='signatories', many=True, read_only=True)

    class Meta:
        model = BankDetail
        fields = ['id','project', 'bank', 'bank_name', 'branch', 'signatories', 'signatories_details']
