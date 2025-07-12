from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from projects.models.project import Project
from projects.models.Installment_Payment.account_photos import AccountPhoto
from projects.serializers.Installment_Payment.account_photos import AccountPhotoSerializer

class AccountPhotoViewSet(viewsets.ModelViewSet):
    queryset = AccountPhoto.objects.filter(is_active=True)
    serializer_class = AccountPhotoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        project_sn = self.kwargs.get('serial_number')  # from URL path
        if project_sn:
            qs = qs.filter(project__serial_number=project_sn)
        return qs

    def perform_create(self, serializer):
        project_sn = self.kwargs.get('serial_number')  # from URL path
        if not project_sn:
            raise ValidationError({"detail": "Project serial_number is required in URL."})

        try:
            project = Project.objects.get(serial_number=project_sn)
        except Project.DoesNotExist:
            raise ValidationError({"detail": f"Project with serial_number={project_sn} not found."})

        serializer.save(project=project)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
