from rest_framework import serializers

class ThirdInstallmentRowSerializer(serializers.Serializer):
    serial_no = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateField()
    status = serializers.CharField()
    file_uploaded_name = serializers.CharField()
    remarks = serializers.CharField(allow_null=True)