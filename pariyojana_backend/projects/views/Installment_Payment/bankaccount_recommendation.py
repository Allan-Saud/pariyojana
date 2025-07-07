from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError
from projects.models.project import Project
from projects.models.Installment_Payment.bankaccount_recommendation import BankAccountRecommendation
from projects.serializers.Installment_Payment.bankaccount_recommendation import BankAccountRecommendationSerializer

class BankAccountRecommendationViewSet(viewsets.ModelViewSet):
    queryset = BankAccountRecommendation.objects.filter(is_active=True).order_by('-date')
    serializer_class = BankAccountRecommendationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = super().get_queryset()
        project_sn = self.request.query_params.get('project')
        if project_sn:
            qs = qs.filter(project__serial_number=project_sn)
        return qs

    def perform_create(self, serializer):
        project_sn = self.request.query_params.get('project')
        if not project_sn:
            raise ValidationError({"detail": "Query parameter 'project' is required."})

        try:
            project = Project.objects.get(serial_number=project_sn)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={project_sn} not found."})

        serializer.save(project=project)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()  # assumes your model has a soft_delete() method
        return Response(status=status.HTTP_204_NO_CONTENT)




# GET /6/bank-account-recommendation/?project=6 — list bank account recommendations for project 6

# POST /6/bank-account-recommendation/?project=6 — create new linked to project 6

# DELETE /bank-account-recommendation/{id}/ — soft delete an entry