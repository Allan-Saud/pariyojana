# projects/serializers/Installment_Payment/first_installment.py
from rest_framework import serializers

class FirstInstallmentRowSerializer(serializers.Serializer):
    serial_no = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateField()
    status = serializers.CharField()
    file_uploaded_name = serializers.CharField()
