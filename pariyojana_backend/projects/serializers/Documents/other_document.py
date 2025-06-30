from rest_framework import serializers
from projects.models.Documents.other_document import OtherDocument

class OtherDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDocument
        fields = ['serial_no', 'title', 'created_at']
