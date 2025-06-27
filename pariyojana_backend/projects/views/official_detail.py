# projects/views/official_detail.py

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from projects.models.official_detail import OfficialDetail
from projects.serializers.official_detail import OfficialDetailSerializer

class OfficialDetailViewSet(viewsets.ModelViewSet):
    queryset = OfficialDetail.objects.all().order_by('serial_no')
    serializer_class = OfficialDetailSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        if project_id:
            return self.queryset.filter(project_id=project_id)
        return self.queryset
