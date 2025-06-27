from rest_framework import serializers
from projects.models.operation_location import OperationSitePhoto

class OperationSitePhotoSerializer(serializers.ModelSerializer):
    photo_name = serializers.SerializerMethodField()

    class Meta:
        model = OperationSitePhoto
        fields = [
            'id', 'project', 'serial_no', 'title',
            'photo', 'photo_name',
            'description', 'uploaded_at'
        ]
        read_only_fields = ['title', 'photo_name', 'uploaded_at']

    def get_photo_name(self, obj):
        return obj.photo.name.split("/")[-1] if obj.photo else None
    
    def update(self, instance, validated_data):
        # If photo is explicitly set to None in PATCH request
        if 'photo' in validated_data and validated_data['photo'] is None:
            instance.photo.delete(save=False)  # Delete the file from storage
            instance.photo = None

        return super().update(instance, validated_data)
