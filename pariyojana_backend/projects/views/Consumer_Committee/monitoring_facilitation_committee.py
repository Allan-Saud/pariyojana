from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from projects.models.project import Project
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember
from projects.serializers.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMemberSerializer

def initialize_monitoring_committee_for_project(project):
    default_posts = [
        "संयोजक",
        "सदस्य सचिव",
        "सदस्य",
        "सदस्य",
        "सदस्य",
        "सदस्य",
    ]

    for idx, post in enumerate(default_posts, start=1):
        MonitoringFacilitationCommitteeMember.objects.get_or_create(
            project=project,
            serial_no=idx,
            defaults={
                'post': post,
                'full_name': None,
                'gender': None,
                'address': None,
                'citizenship_no': None,
                'contact_no': None,
                'citizenship_front': None,
                'citizenship_back': None,
            }
        )


# class MonitoringFacilitationCommitteeViewSet(viewsets.ModelViewSet):
#     serializer_class = MonitoringFacilitationCommitteeMemberSerializer

#     def get_queryset(self):
#         serial_number = self.kwargs.get('serial_number')
#         try:
#             project = Project.objects.get(serial_number=serial_number)
#         except Project.DoesNotExist:
#             raise NotFound("Project not found.")
#         return MonitoringFacilitationCommitteeMember.objects.filter(project=project).order_by('serial_no')

#     def perform_create(self, serializer):
#         serial_number = self.kwargs.get('serial_number')
#         try:
#             project = Project.objects.get(serial_number=serial_number)
#         except Project.DoesNotExist:
#             raise NotFound("Project not found.")
#         serializer.save(project=project)


class MonitoringFacilitationCommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = MonitoringFacilitationCommitteeMemberSerializer

    def get_queryset(self):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise NotFound("Project not found.")

        qs = MonitoringFacilitationCommitteeMember.objects.filter(project=project)
        
        if not qs.exists():
            initialize_monitoring_committee_for_project(project)
            qs = MonitoringFacilitationCommitteeMember.objects.filter(project=project)

        return qs.order_by('serial_no')

    def perform_create(self, serializer):
        serial_number = self.kwargs.get('serial_number')
        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        serializer.save(project=project)
