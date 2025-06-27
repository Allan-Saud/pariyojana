# views/consumer_committee_details.py

from rest_framework import viewsets
from projects.models.consumer_committee_details import ConsumerCommitteeDetail
from projects.serializers.consumer_committee_details import ConsumerCommitteeDetailSerializer
from rest_framework.permissions import IsAuthenticated

class ConsumerCommitteeDetailViewSet(viewsets.ModelViewSet):
    queryset = ConsumerCommitteeDetail.objects.filter(is_active=True)
    serializer_class = ConsumerCommitteeDetailSerializer
    permission_classes = [IsAuthenticated]
