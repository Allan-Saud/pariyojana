# # views/consumer_committee_details.py

from rest_framework import viewsets
from projects.models.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetail
from projects.serializers.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetailSerializer
from rest_framework.permissions import IsAuthenticated

class ConsumerCommitteeDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumerCommitteeDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')
        queryset = ConsumerCommitteeDetail.objects.filter(is_active=True)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset
