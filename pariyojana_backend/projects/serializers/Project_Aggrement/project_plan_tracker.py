# from rest_framework import serializers

# class ProjectPlanTrackerRowSerializer(serializers.Serializer):
#     serial_no = serializers.IntegerField()
#     title = serializers.CharField()
#     date = serializers.DateField()
#     status = serializers.CharField()
#     file_uploaded_name = serializers.CharField()

from rest_framework import serializers

class ProjectPlanTrackerRowSerializer(serializers.Serializer):
    serial_no = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateField()
    status = serializers.CharField()
    file_uploaded_name = serializers.CharField()
    file_url = serializers.SerializerMethodField()

    def get_file_url(self, obj):
        request = self.context.get('request')
        file_url = obj.get('file_url')
        if file_url:
            # file_url already absolute from view, just return it
            return file_url
        return None
