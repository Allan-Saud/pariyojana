from rest_framework import viewsets
from authentication.models import VerificationLog
from authentication.serializers import VerificationLogSerializer

class VerificationLogViewSet(viewsets.ModelViewSet):
    queryset = VerificationLog.objects.all().order_by('-id')
    serializer_class = VerificationLogSerializer
