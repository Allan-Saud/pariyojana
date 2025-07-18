# views.py
from rest_framework import viewsets
from .models import CostEstimationCalculation
from .serializers import CostEstimationCalculationSerializer
from projects.models.project import Project
from rest_framework.decorators import action
from rest_framework.response import Response

class CostEstimationCalculationViewSet(viewsets.ModelViewSet):
    serializer_class = CostEstimationCalculationSerializer

    def get_queryset(self):
        project_serial = self.kwargs.get('serial_number')
        return CostEstimationCalculation.objects.filter(project__serial_number=project_serial)

    def perform_create(self, serializer):
        project_serial = self.kwargs.get('serial_number')
        project = Project.objects.get(serial_number=project_serial)
        serializer.save(project=project)

    
    @action(detail=True, methods=['get'])
    def formatted(self, request, serial_number=None, pk=None):
        instance = self.get_object()
        base = instance.total_without_vat
        vat = instance.vat_amount
        ps = instance.ps_amount
        contingency = instance.contingency_amount

        subtotal = base + vat
        grand_total = subtotal + ps + contingency


        data = {
            "क. जम्मा रकम": f"{base:.2f}",
            "ख. १३% मु.अ.कर": f"{vat:.2f}",
            "ग. कुल जम्मा (क+ख)": f"{subtotal:.2f}",
            "घ. कुल जम्मा (ग+A)": f"{grand_total:.2f}",
        }
        return Response(data)


