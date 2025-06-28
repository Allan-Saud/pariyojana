from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from projects.models.Operation_Location.operation_location import OperationSitePhoto
from projects.serializers.Operatio_Location.operation_location import OperationSitePhotoSerializer

class OperationSitePhotoViewSet(viewsets.ModelViewSet):
    queryset = OperationSitePhoto.objects.all()
    serializer_class = OperationSitePhotoSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = super().get_queryset()
        project_id = self.request.query_params.get('project')
        if project_id:
            qs = qs.filter(project_id=project_id)
        return qs
