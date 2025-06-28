from rest_framework import viewsets
from projects.models.Program_Details.beneficiary_details import BeneficiaryDetail
from projects.serializers.Program_Details.beneficiary_details import BeneficiaryDetailSerializer
from rest_framework.response import Response  # <-- add this line
from rest_framework import status 

class BeneficiaryDetailViewSet(viewsets.ModelViewSet):
    queryset = BeneficiaryDetail.objects.all()
    serializer_class = BeneficiaryDetailSerializer

    def create(self, request, *args, **kwargs):
        # To support multiple objects in POST (list), you can override create()
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
