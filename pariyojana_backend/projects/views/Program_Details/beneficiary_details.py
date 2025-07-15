
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from projects.models.Program_Details.beneficiary_details import BeneficiaryDetail
from projects.serializers.Program_Details.beneficiary_details import BeneficiaryDetailSerializer
from projects.models.project import Project
from rest_framework.decorators import action


class BeneficiaryDetailViewSet(viewsets.ModelViewSet):
    queryset = BeneficiaryDetail.objects.all()
    serializer_class = BeneficiaryDetailSerializer

    def get_queryset(self):
        serial_number = self.kwargs.get('serial_number') or self.request.query_params.get('serial_number')
        if serial_number:
            return BeneficiaryDetail.objects.filter(project__serial_number=serial_number)
        return BeneficiaryDetail.objects.none()

    def list(self, request, *args, **kwargs):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            return Response({"detail": "Project serial_number is required in URL."}, status=400)

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            return Response({"detail": f"Project with serial_number={serial_number} not found."}, status=404)

        existing = BeneficiaryDetail.objects.filter(project__serial_number=serial_number)
        existing_map = {b.title: b for b in existing}

        result = []
        for key, _ in BeneficiaryDetail.CATEGORY_CHOICES:
            if key in existing_map:
                result.append(self.get_serializer(existing_map[key]).data)
            else:
                result.append({
                    "title": key,
                    "female": 0,
                    "male": 0,
                    "other": 0,
                    "total": 0,
                    "project": project.serial_number,
                })

        return Response(result)

    
    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serial_number = self.kwargs.get('serial_number') or request.query_params.get('serial_number')

        if not serial_number:
            raise ValidationError({"detail": "Project serial_number is required."})

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={serial_number} not found."})

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)

        if is_many:
            instances = []
            for data in serializer.validated_data:
                female = data.get('female', 0) or 0
                male = data.get('male', 0) or 0
                other = data.get('other', 0) or 0
                total = female + male + other

                instance = BeneficiaryDetail(
                    project=project,
                    title=data['title'],
                    female=female,
                    male=male,
                    other=other,
                    total=total
                )
                instances.append(instance)

            BeneficiaryDetail.objects.bulk_create(instances)
            return Response(self.get_serializer(instances, many=True).data, status=status.HTTP_201_CREATED)

        else:
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    # def bulk_update(self, request, serial_number=None):
    #     data = request.data
    #     if not isinstance(data, list):
    #         return Response({"detail": "Expected a list of items for bulk update."}, status=400)

    #     updated_items = []
    #     for item in data:
    #         beneficiary_id = item.get('id')
    #         if not beneficiary_id:
    #             return Response({"detail": "Each item must contain 'id'."}, status=400)

    #         try:
    #             instance = BeneficiaryDetail.objects.get(id=beneficiary_id, project__serial_number=serial_number)
    #         except BeneficiaryDetail.DoesNotExist:
    #             return Response({"detail": f"Beneficiary {beneficiary_id} not found for project {serial_number}."}, status=404)

    #         serializer = self.get_serializer(instance, data=item, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         updated_items.append(serializer.data)

    #     return Response(updated_items, status=status.HTTP_200_OK)
    
    def bulk_update(self, request, serial_number=None):
        data = request.data
        if not isinstance(data, list):
            return Response({"detail": "Expected a list of items for bulk update."}, status=400)

        updated_items = []
        project = Project.objects.get(serial_number=serial_number)
        
        for item in data:
            title = item.get('title')
            if not title:
                return Response({"detail": "Each item must contain 'title'."}, status=400)

            # Get or create the beneficiary record
            instance, created = BeneficiaryDetail.objects.get_or_create(
                project=project,
                title=title,
                defaults={
                    'female': item.get('female', 0),
                    'male': item.get('male', 0),
                    'other': item.get('other', 0)
                }
            )

            # Update if not created
            if not created:
                serializer = self.get_serializer(instance, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                updated_items.append(serializer.data)
            else:
                updated_items.append(self.get_serializer(instance).data)

        return Response(updated_items, status=status.HTTP_200_OK)
    
    
    
    @action(detail=False, methods=['post'], url_path='update-all')
    def update_all_beneficiaries(self, request, serial_number=None):
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            return Response({"detail": "Project not found"}, status=404)

        # Get all existing records for this project
        existing = {b.title: b for b in BeneficiaryDetail.objects.filter(project=project)}
        
        response_data = []
        for category_data in request.data:
            title = category_data.get('title')
            if not title:
                continue
                
            # Get or create the record
            if title in existing:
                instance = existing[title]
                serializer = self.get_serializer(instance, data=category_data, partial=True)
            else:
                serializer = self.get_serializer(data=category_data)
            
            serializer.is_valid(raise_exception=True)
            serializer.save(project=project)
            response_data.append(serializer.data)
        
        return Response(response_data, status=200)

