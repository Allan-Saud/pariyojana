# from rest_framework import serializers

# class ProjectAgreementWorkorderRowSerializer(serializers.Serializer):
#     file_url = request.build_absolute_uri(instance.file.url) if instance.file else None
#     serial_no = serializers.IntegerField()
#     title = serializers.CharField()
#     date = serializers.DateField()
#     status = serializers.CharField()  # "अपलोड गरिएको" or blank
#     file_uploaded_name = serializers.CharField()

from rest_framework import serializers

class ProjectAgreementWorkorderRowSerializer(serializers.Serializer):
    serial_no = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateField()
    status = serializers.CharField()
    file_uploaded_name = serializers.CharField()
    file_url = serializers.SerializerMethodField()

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.get('file'):
            file_path = obj['file']
            if request:
                return request.build_absolute_uri(file_path)
            else:
                return file_path
        return None

