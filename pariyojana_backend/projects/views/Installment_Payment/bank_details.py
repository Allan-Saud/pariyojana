from rest_framework import viewsets
from projects.models.Installment_Payment.bank_details import BankDetail
from projects.serializers.Installment_Payment.bank_details import BankDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from projects.models.project import Project
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
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
        
    def partial_update(self, request, *args, **kwargs):
        serial_number = kwargs.get('serial_number')
        pk = kwargs.get('pk')

        if not serial_number:
            return Response({"detail": "Project serial_number is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not pk:
            return Response({"detail": "Bank detail id (pk) is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = BankDetail.objects.get(pk=pk, project__serial_number=serial_number)
        except BankDetail.DoesNotExist:
            raise NotFound(f"Bank detail not found for project {serial_number} and id {pk}")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


# GET /6/bank-details/ — list bank details of project with serial_number=6
# http://127.0.0.1:8000/api/projects/6/bank-details/3/  patch
# POST /6/bank-details/ — add new bank detail to project with serial_number=6 
# (send data in request body, and make sure to include ?project=6 query param or handle project assignment in your viewset).