from rest_framework import serializers
from projects.models.Installment_Payment.first_installment import FirstInstallmentDocument
from projects.constants import FIRST_INSTALLMENT_TITLES

class FirstInstallmentDocumentSerializer(serializers.ModelSerializer):
    स्थिति = serializers.SerializerMethodField()
    मिति = serializers.DateField(source='uploaded_at', read_only=True)
    शिर्षक = serializers.SerializerMethodField()

    class Meta:
        model = FirstInstallmentDocument
        fields = ['serial_number', 'शिर्षक', 'मिति', 'स्थिति', 'remarks', 'file']

    def get_स्थिति(self, obj):
        return obj.status()
    


    def get_शिर्षक(self, obj):
        title_map = {item["serial_no"]: item["title"] for item in FIRST_INSTALLMENT_TITLES}
        return title_map.get(obj.serial_number, "")

