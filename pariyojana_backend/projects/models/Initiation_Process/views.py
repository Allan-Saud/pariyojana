from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from projects.models.project import Project
from projects.models.Initiation_Process.initiation_process import InitiationProcess
from projects.serializers.Initiation_Process.initiation_process import InitiationProcessSerializer

class InitiationProcessViewSet(viewsets.ModelViewSet):
    queryset = InitiationProcess.objects.all()
    serializer_class = InitiationProcessSerializer

    def perform_create(self, serializer):
        project_id = self.kwargs.get('serial_number')
        project = get_object_or_404(Project, pk=project_id)
        serializer.save(project=project)
