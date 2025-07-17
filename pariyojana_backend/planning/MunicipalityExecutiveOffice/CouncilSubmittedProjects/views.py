from rest_framework import viewsets
from rest_framework.response import Response
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.models import CouncilSubmittedProject
from planning.MunicipalityExecutiveOffice.CouncilSubmittedProjects.serializers import CouncilSubmittedProjectsSerializer

class CouncilSubmittedProjectViewSet(viewsets.ModelViewSet):
    queryset = CouncilSubmittedProject.objects.all()
    serializer_class = CouncilSubmittedProjectsSerializer
   
    def get_queryset(self):
        queryset = CouncilSubmittedProject.objects.all()
        
        return queryset