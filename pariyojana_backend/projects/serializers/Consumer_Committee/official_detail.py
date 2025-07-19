# # projects/serializers/official_detail.py

from rest_framework import serializers
from projects.models.Consumer_Committee.official_detail import OfficialDetail

# class OfficialDetailSerializer(serializers.ModelSerializer):
#     citizenship_front_url = serializers.SerializerMethodField()
#     citizenship_back_url = serializers.SerializerMethodField()

#     class Meta:
#         model = OfficialDetail
#         fields = [
#             'id','post', 'full_name', 'address',
#             'contact_no', 'gender', 'citizenship_no',
#             'citizenship_front', 'citizenship_back',
#             'citizenship_front_url', 'citizenship_back_url',
#             'created_at', 'updated_at',
#         ]
#         read_only_fields = ['project', 'serial_no']

#     def get_citizenship_front_url(self, obj):
#         if obj.citizenship_front:
#             return obj.citizenship_front.url
#         return None

#     def get_citizenship_back_url(self, obj):
#         if obj.citizenship_back:
#             return obj.citizenship_back.url
#         return None

# projects/serializers/official_detail.py




class OfficialDetailSerializer(serializers.ModelSerializer):
    citizenship_front_url = serializers.SerializerMethodField()
    citizenship_back_url = serializers.SerializerMethodField()
    
    class Meta:
        model = OfficialDetail
        fields = [
            'id',
            'serial_no',
            'post',
            'full_name',
            'address',
            'contact_no',
            'gender',
            'citizenship_no',
            'citizenship_front',
            'citizenship_back',
            'citizenship_front_url',
            'citizenship_back_url',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_citizenship_front_url(self, obj):
        if obj.citizenship_front:
            return self.context['request'].build_absolute_uri(obj.citizenship_front.url)
        return None

    def get_citizenship_back_url(self, obj):
        if obj.citizenship_back:
            return self.context['request'].build_absolute_uri(obj.citizenship_back.url)
        return None

    def validate_serial_no(self, value):
        project = self.context.get('project')
        if not project:
            raise serializers.ValidationError("Project context is required")
        
        # Check for duplicate serial numbers within the same project
        queryset = OfficialDetail.objects.filter(project=project, serial_no=value)
        
        # If updating, exclude current instance
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError(f"Serial number {value} already exists for this project")
        
        return value

    def validate_contact_no(self, value):
        # Basic validation for Nepali phone numbers
        if not value.isdigit() or len(value) < 7 or len(value) > 15:
            raise serializers.ValidationError("Contact number should be 7-15 digits")
        return value

    def validate_citizenship_no(self, value):
        if not value.strip():
            raise serializers.ValidationError("Citizenship number is required")
        return value


class OfficialDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialDetail
        fields = [
            'serial_no',
            'post',
            'full_name',
            'address',
            'contact_no',
            'gender',
            'citizenship_no',
            'citizenship_front',
            'citizenship_back'
        ]

    def validate_serial_no(self, value):
        project = self.context.get('project')
        if not project:
            raise serializers.ValidationError("Project context is required")
        
        # Check for duplicate serial numbers within the same project
        queryset = OfficialDetail.objects.filter(project=project, serial_no=value)
        
        # If updating, exclude current instance
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError(f"Serial number {value} already exists for this project")
        
        return value

    def validate_contact_no(self, value):
        # Basic validation for Nepali phone numbers
        if not value.isdigit() or len(value) < 7 or len(value) > 15:
            raise serializers.ValidationError("Contact number should be 7-15 digits")
        return value


class OfficialDetailListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views"""
    class Meta:
        model = OfficialDetail
        fields = [
            'id',
            'serial_no',
            'post',
            'full_name',
            'gender',
            'contact_no',
            'created_at'
        ]
