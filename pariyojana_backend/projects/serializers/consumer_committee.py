from rest_framework import serializers

class ConsumerCommitteeRowSerializer(serializers.Serializer):
    serial_no = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateField()
    status = serializers.CharField()  #स्थिति: अपलोड गरिएको or blank
    file_uploaded_name = serializers.CharField()
