# projects/serializers/official_detail.py

from rest_framework import serializers
from projects.models.Consumer_Committee.official_detail import OfficialDetail

class OfficialDetailSerializer(serializers.ModelSerializer):
    citizenship_front_url = serializers.SerializerMethodField()
    citizenship_back_url = serializers.SerializerMethodField()

    class Meta:
        model = OfficialDetail
        fields = [
            'id','post', 'full_name', 'address',
            'contact_no', 'gender', 'citizenship_no',
            'citizenship_front', 'citizenship_back',
            'citizenship_front_url', 'citizenship_back_url',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['project', 'serial_no']

    def get_citizenship_front_url(self, obj):
        if obj.citizenship_front:
            return obj.citizenship_front.url
        return None

    def get_citizenship_back_url(self, obj):
        if obj.citizenship_back:
            return obj.citizenship_back.url
        return None
