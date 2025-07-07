from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from projects.models.Program_Details.beneficiary_details import BeneficiaryDetail
from projects.serializers.Program_Details.beneficiary_details import BeneficiaryDetailSerializer
from projects.models.project import Project

class BeneficiaryDetailViewSet(viewsets.ModelViewSet):
    queryset = BeneficiaryDetail.objects.all()
    serializer_class = BeneficiaryDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Support nested URL: /projects/<serial_number>/beneficiaries/
        serial_number = self.kwargs.get('serial_number')
        if serial_number:
            queryset = queryset.filter(project__serial_number=serial_number)
        
        # Also support query param: ?project_id=6
        query_param = self.request.query_params.get('project_id')
        if query_param:
            queryset = queryset.filter(project__serial_number=query_param)

        return queryset

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        project_id = self.kwargs.get('serial_number') or request.query_params.get('project_id')

        if not project_id:
            raise ValidationError({"detail": "Project ID is required either in URL or as query param."})

        try:
            project = Project.objects.get(serial_number=project_id)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={project_id} does not exist."})

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)

        if is_many:
            instances = [BeneficiaryDetail(project=project, **data) for data in serializer.validated_data]
            BeneficiaryDetail.objects.bulk_create(instances)
            return Response(self.get_serializer(instances, many=True).data, status=status.HTTP_201_CREATED)
        else:
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    from rest_framework import status

    @action(detail=False, methods=['get'], url_path='by-project/(?P<project_id>\\d+)/')
    def by_project(self, request, project_id=None):
        if request.method == 'GET':
            beneficiaries = BeneficiaryDetail.objects.filter(project__serial_number=project_id)
            serializer = self.get_serializer(beneficiaries, many=True)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            data = request.data
            if not isinstance(data, list):
                return Response({"detail": "Expected a list of items for bulk update"}, status=status.HTTP_400_BAD_REQUEST)

            response_data = []
            for item in data:
                beneficiary_id = item.get('id')
                if not beneficiary_id:
                    return Response({"detail": "Each item must contain 'id' field"}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    beneficiary = BeneficiaryDetail.objects.get(id=beneficiary_id, project__serial_number=project_id)
                except BeneficiaryDetail.DoesNotExist:
                    return Response({"detail": f"Beneficiary with id {beneficiary_id} not found in this project."}, status=status.HTTP_404_NOT_FOUND)

                serializer = self.get_serializer(beneficiary, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response_data.append(serializer.data)

            return Response(response_data, status=status.HTTP_200_OK)
        
        
        
        
    def bulk_update(self, request, serial_number=None):
            data = request.data
            if not isinstance(data, list):
                return Response({"detail": "Expected a list of items for bulk update."}, status=400)

            updated_items = []

            for item in data:
                beneficiary_id = item.get('id')
                if not beneficiary_id:
                    return Response({"detail": "Each item must contain 'id'."}, status=400)

                try:
                    instance = BeneficiaryDetail.objects.get(id=beneficiary_id, project__serial_number=serial_number)
                except BeneficiaryDetail.DoesNotExist:
                    return Response({"detail": f"Beneficiary {beneficiary_id} not found in project {serial_number}."}, status=404)

                serializer = self.get_serializer(instance, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                updated_items.append(serializer.data)

            return Response(updated_items, status=status.HTTP_200_OK)
