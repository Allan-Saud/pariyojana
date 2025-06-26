# projects/views/initiation_process.py

from rest_framework import viewsets
from projects.models.initiation_process import InitiationProcess
from projects.serializers.initiation_process import InitiationProcessSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class InitiationProcessViewSet(viewsets.ModelViewSet):
    queryset = InitiationProcess.objects.all()
    serializer_class = InitiationProcessSerializer

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
