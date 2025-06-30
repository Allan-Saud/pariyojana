from rest_framework import serializers

class ProjectAgreementWorkorderRowSerializer(serializers.Serializer):
    serial_no = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateField()
    status = serializers.CharField()  # "अपलोड गरिएको" or blank
    file_uploaded_name = serializers.CharField()
