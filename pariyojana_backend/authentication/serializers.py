
# from rest_framework import serializers
# from authentication.models import VerificationLog 

# class VerificationLogSerializer(serializers.ModelSerializer):
#     project_name = serializers.CharField(source='project.name', read_only=True)
#     file_title = serializers.SerializerMethodField() 
#     status_nepali = serializers.SerializerMethodField()
#     class Meta:
#         model = VerificationLog
#         fields = '__all__'
        
#     def get_file_title(self, obj):
#         # Split the title by ' - ' and return the last part
#         parts = obj.file_title.split(' - ')
#         return parts[-1] if len(parts) > 1 else obj.file_title
    
#     def get_status_nepali(self, obj):
#         return obj.get_status_nepali()


from rest_framework import serializers
from authentication.models import VerificationLog

class VerificationLogSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    status_nepali = serializers.SerializerMethodField()
    file_title_display = serializers.SerializerMethodField()

    class Meta:
        model = VerificationLog
        fields = [
            'id', 'project', 'project_name',
            'file_title', 'file_title_display',  # keep both raw and parsed if needed
            'uploader_role', 'uploader_name', 'file_path',
            'status', 'status_nepali', 'remarks',
            'checker', 'approver', 'created_at',
            'source_model', 'source_id'
        ]

    def get_file_title_display(self, obj):
        """ Returns the last part of the file_title after splitting with ' - ' """
        parts = obj.file_title.split(' - ')
        return parts[-1] if len(parts) > 1 else obj.file_title

    def get_status_nepali(self, obj):
        return obj.get_status_nepali()
