from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from projects.models.Operation_Location.operation_location import OperationSitePhoto
from projects.serializers.Operatio_Location.operation_location import OperationSitePhotoSerializer
from projects.models.project import Project


class OperationSitePhotoViewSet(viewsets.ModelViewSet):
    queryset = OperationSitePhoto.objects.all()
    serializer_class = OperationSitePhotoSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = super().get_queryset()
        serial_number = self.kwargs.get('serial_number') or self.request.query_params.get('project')
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

    # def list(self, request, *args, **kwargs):
    #     serial_number = self.kwargs.get('serial_number') or self.request.query_params.get('project')

    #     if not serial_number:
    #         return Response({"detail": "Project 'serial_number' is required as URL param or query param."}, status=400)

    #     try:
    #         project = Project.objects.get(serial_number=serial_number)
    #     except Project.DoesNotExist:
    #         return Response({"detail": f"Project with serial_number={serial_number} not found."}, status=404)

    #     # Get existing photos
    #     existing_photos = OperationSitePhoto.objects.filter(project=project)
    #     existing_map = {photo.serial_no: photo for photo in existing_photos}

    #     # Import your serial choices from model
    #     from projects.models.Operation_Location.operation_location import SERIAL_CHOICES

    #     result = []
    #     for serial, label in SERIAL_CHOICES:
    #         if serial in existing_map:
    #             instance = existing_map[serial]
    #             result.append(self.get_serializer(instance).data)
    #         else:
    #             result.append({
    #                 "serial": serial,
    #                 "caption": "",
    #                 "image": None,
    #                 "project": project.serial_number
    #             })

    #     return Response(result)
    
    def list(self, request, *args, **kwargs):
        serial_number = self.kwargs.get('serial_number') or request.query_params.get('project')

        if not serial_number:
            return Response({"detail": "Project 'serial_number' is required as URL param or query param."}, status=400)

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            return Response({"detail": f"Project with serial_number={serial_number} not found."}, status=404)

        existing_photos = OperationSitePhoto.objects.filter(project=project)
        existing_map = {photo.serial_no: photo for photo in existing_photos}

        from projects.models.Operation_Location.operation_location import SERIAL_CHOICES

        result = []
        for serial, label in SERIAL_CHOICES:
            if serial in existing_map:
                instance = existing_map[serial]
                result.append(self.get_serializer(instance).data)
            else:
                result.append({
                    'id': None,
                    'project': project.serial_number, 
                    'serial_no': serial,
                    'title': label,
                    'photo': None,
                    'photo_name': None,
                    'description': "",
                    'uploaded_at': None
                })

        return Response(result)

