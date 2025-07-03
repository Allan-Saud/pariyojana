from rest_framework import viewsets
from .models import ProjectsApprovedByMunicipal
from .serializers import ProjectsApprovedByMunicipalSerializer

class ProjectsApprovedByMunicipalViewSet(viewsets.ModelViewSet):
    queryset = ProjectsApprovedByMunicipal.objects.all()
    serializer_class = ProjectsApprovedByMunicipalSerializer
