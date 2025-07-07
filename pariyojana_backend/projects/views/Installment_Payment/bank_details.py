from rest_framework import viewsets
from projects.models.Installment_Payment.bank_details import BankDetail
from projects.serializers.Installment_Payment.bank_details import BankDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from projects.models.project import Project

class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        # Try nested URL param first
        serial_number = self.kwargs.get('serial_number')
        # fallback to query param
        if not serial_number:
            serial_number = self.request.query_params.get('project')

        if serial_number:
            qs = qs.filter(project__serial_number=serial_number)
        return qs

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number') or self.request.query_params.get('project')
        if not serial_number:
            raise ValidationError({"detail": "Project 'serial_number' is required as URL param or query param."})

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={serial_number} not found."})

        serializer.save(project=project)


# GET /6/bank-details/ — list bank details of project with serial_number=6

# POST /6/bank-details/ — add new bank detail to project with serial_number=6 
# (send data in request body, and make sure to include ?project=6 query param or handle project assignment in your viewset).