from rest_framework import serializers
from projects.models.Documents.other_document import OtherDocument

class OtherDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDocument
        fields = ['serial_no', 'title', 'created_at', 'project']  # add project if you want to allow it in POST
        read_only_fields = ['created_at']

