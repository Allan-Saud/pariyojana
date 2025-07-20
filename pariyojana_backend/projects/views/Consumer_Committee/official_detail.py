from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.serializers.Consumer_Committee.official_detail import OfficialDetailSerializer
from projects.models.project import Project
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from django.db import transaction


def initialize_officials_for_project(project):
    default_posts = [
        "अध्यक्ष",
        "सचिव",
        "कोषाध्यक्ष",
        "सदस्य",
        "सदस्य",
        "सदस्य",
        "सदस्य"
    ]

    with transaction.atomic():
        for idx, post in enumerate(default_posts, start=1):
            OfficialDetail.objects.get_or_create(
                project=project,
                serial_no=idx,
                defaults={
                    'post': post,
                    'full_name': None,
                    'address': None,
                    'contact_no': None,
                    'gender': None,
                    'citizenship_no': None,
                    'citizenship_front': None,
                    'citizenship_back': None,
                }
            )


# class OfficialDetailViewSet(viewsets.ModelViewSet):
#     serializer_class = OfficialDetailSerializer

#     def get_queryset(self):
#         serial_number = self.kwargs.get('serial_number')
#         try:
#             project = Project.objects.get(serial_number=serial_number)
#         except Project.DoesNotExist:
#             raise NotFound("Project not found")
#         return OfficialDetail.objects.filter(project=project).order_by('serial_no')

#     def perform_create(self, serializer):
#         serial_number = self.kwargs.get('serial_number')
#         try:
#             project = Project.objects.get(serial_number=serial_number)
#         except Project.DoesNotExist:
#             raise NotFound("Project not found")
#         serializer.save(project=project)

class OfficialDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OfficialDetailSerializer

    def get_queryset(self):
        serial_number = self.kwargs.get('serial_number')
        project = Project.objects.filter(serial_number=serial_number).first()
        if not project:
            raise NotFound("Project not found")
        # Initialize records if not already present
        if not OfficialDetail.objects.filter(project=project).exists():
            initialize_officials_for_project(project)
        return OfficialDetail.objects.filter(project=project).order_by('serial_no')

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        project = Project.objects.get(serial_number=serial_number)
        serializer.save(project=project)
