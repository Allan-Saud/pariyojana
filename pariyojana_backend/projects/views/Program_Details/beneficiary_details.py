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
        project_id = request.query_params.get('project_id')

        if not project_id:
            raise ValidationError({"detail": "Query parameter 'project_id' is required."})

        try:
            project = Project.objects.get(serial_number=project_id)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={project_id} does not exist."})

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)

        if is_many:
            for item in serializer.validated_data:
                item['project'] = project
            instances = [BeneficiaryDetail(**data) for data in serializer.validated_data]
            BeneficiaryDetail.objects.bulk_create(instances)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='by-project/(?P<project_id>\d+)')
    def by_project(self, request, project_id=None):
        beneficiaries = BeneficiaryDetail.objects.filter(project__serial_number=project_id)
        serializer = self.get_serializer(beneficiaries, many=True)
        return Response(serializer.data)
