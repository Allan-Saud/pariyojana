# serializers/consumer_committee_details.py

from rest_framework import serializers
from projects.models.consumer_committee_details import ConsumerCommitteeDetail

class ConsumerCommitteeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerCommitteeDetail
        fields = '__all__'
