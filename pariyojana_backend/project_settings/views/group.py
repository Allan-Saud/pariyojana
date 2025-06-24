from rest_framework import viewsets
from project_settings.models.group import Group
from project_settings.serializers.group import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
