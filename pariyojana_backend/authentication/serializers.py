
from rest_framework import serializers
from authentication.models import VerificationLog 

class VerificationLogSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    file_title = serializers.SerializerMethodField() 
    class Meta:
        model = VerificationLog
        fields = '__all__'
        
    def get_file_title(self, obj):
        # Split the title by ' - ' and return the last part
        parts = obj.file_title.split(' - ')
        return parts[-1] if len(parts) > 1 else obj.file_title
