from rest_framework import viewsets
from authentication.worker_model import Person
from authentication.worker_serializer import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonSerializer
