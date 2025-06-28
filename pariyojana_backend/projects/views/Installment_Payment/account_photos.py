from rest_framework import viewsets, status
from rest_framework.response import Response
from projects.models.Installment_Payment.account_photos import AccountPhoto
from projects.serializers.Installment_Payment.account_photos import AccountPhotoSerializer

class AccountPhotoViewSet(viewsets.ModelViewSet):
    queryset = AccountPhoto.objects.filter(is_active=True)
    serializer_class = AccountPhotoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
