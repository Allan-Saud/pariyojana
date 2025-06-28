# projects/serializers/monitoring_facilitation_committee.py

from rest_framework import serializers
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember

class MonitoringFacilitationCommitteeSerializer(serializers.ModelSerializer):
    citizenship_front_url = serializers.SerializerMethodField()
    citizenship_back_url = serializers.SerializerMethodField()

    class Meta:
        model = MonitoringFacilitationCommitteeMember
        fields = [
            'id', 'project', 'serial_no', 'post', 'full_name',
            'gender', 'address', 'citizenship_no', 'contact_no',
            'citizenship_front', 'citizenship_back',
            'citizenship_front_url', 'citizenship_back_url',
            'created_at', 'updated_at',
        ]

    def get_citizenship_front_url(self, obj):
        return obj.citizenship_front.url if obj.citizenship_front else None

    def get_citizenship_back_url(self, obj):
        return obj.citizenship_back.url if obj.citizenship_back else None
