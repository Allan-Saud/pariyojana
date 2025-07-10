from rest_framework import viewsets, permissions
from projects.models.Documents.documents import Document
from projects.serializers.Documents.documents import DocumentSerializer
from projects.models.project import Project
from django.shortcuts import get_object_or_404

# views.py

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        serial_number = self.kwargs.get('serial_number')
        return Document.objects.filter(project__serial_number=serial_number).order_by('-uploaded_at')

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        project = get_object_or_404(Project, serial_number=serial_number)
        serializer.save(uploaded_by=self.request.user, project=project)

