# projects/views/initiation_process.py

from rest_framework import viewsets
from projects.models.Initiation_Process.initiation_process import InitiationProcess
from projects.serializers.Initiation_Process.initiation_process import InitiationProcessSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from projects.models.project import Project  
from rest_framework import serializers

class InitiationProcessViewSet(viewsets.ModelViewSet):
    queryset = InitiationProcess.objects.all()
    serializer_class = InitiationProcessSerializer
  
  
    def get_queryset(self):
        queryset = super().get_queryset()

        serial_number = self.kwargs.get('serial_number')
        if serial_number:
            queryset = queryset.filter(project__serial_number=serial_number)

        query_param = self.request.query_params.get('project_id')
        if query_param:
            queryset = queryset.filter(project__serial_number=query_param)

        return queryset

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
            serializer.save(project=project)
        except Project.DoesNotExist:
            raise serializers.ValidationError({"project": "Project with this serial number does not exist."})


    @action(detail=True, methods=["post"])
    def confirm_initiation(self, request, pk=None):
        instance = self.get_object()

        if instance.is_confirmed:
            return Response({
                "message": f"{instance.initiation_method} परियोजना सुचारु भएको छ ।",
                "enabled_steps": [
                    "उपभोक्ता समिति गठन",
                    "योजना सम्झौता",
                    "किस्ता भुक्तानी सम्बन्धी"
                ]
            })

        return Response({
            "message": "प्रक्रिया पुष्टि गरिएको छैन। कृपया OK थिच्नुहोस्।"
        }, status=status.HTTP_400_BAD_REQUEST)

