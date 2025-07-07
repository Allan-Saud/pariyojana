from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError, NotFound
from projects.models.project import Project
from projects.models.Installment_Payment.bankaccount_recommendation import BankAccountRecommendation
from projects.serializers.Installment_Payment.bankaccount_recommendation import BankAccountRecommendationSerializer


class BankAccountRecommendationViewSet(viewsets.ModelViewSet):
    queryset = BankAccountRecommendation.objects.all().order_by('-date')
    serializer_class = BankAccountRecommendationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = super().get_queryset()
        serial_number = self.kwargs.get('serial_number')
        print("Serial number in get_queryset:", serial_number)
        if serial_number:
            qs = qs.filter(project__serial_number=serial_number)
        print("Queryset count after filter:", qs.count())
        return qs

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        if not pk:
            # For detail views, pk must be provided
            raise ValidationError({"detail": "ID (pk) is required."})

        obj = queryset.filter(pk=pk).first()
        if not obj:
            raise NotFound("Bank account recommendation not found for this project and id.")
        return obj

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number') or self.request.query_params.get('project')

        if not serial_number:
            raise ValidationError({"detail": "Project 'serial_number' is required as URL param or query param."})

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={serial_number} not found."})

        serializer.save(project=project)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()  # if you have a soft delete method
        return Response(status=status.HTTP_204_NO_CONTENT)

# GET /6/bank-account-recommendation/— list bank account recommendations for project 6

# POST /6/bank-account-recommendation/ — create new linked to project 6

# patch  /6/bank-account-recommendation/{id}/ — soft delete an entry