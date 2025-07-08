from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from planning.WardOffice.WardLevelProject.models import WardLevelProject
from planning.WardOffice.PrioritizedWardLevelProjects.models import PrioritizedWardLevelProject
from planning.WardOffice.WardLevelProject.serializers import WardLevelProjectSerializer
from django.utils import timezone
class WardLevelProjectViewSet(viewsets.ModelViewSet):
    # queryset = WardLevelProject.objects.all()
    serializer_class = WardLevelProjectSerializer
    def get_queryset(self):
        return WardLevelProject.objects.filter(is_deleted=False)

    @action(detail=True, methods=['post'], url_path='prioritize')
    def prioritize(self, request, pk=None):
        try:
            ward_project = self.get_object()

            # Check if already prioritized
            already_exists = PrioritizedWardLevelProject.objects.filter(
                plan_name=ward_project.plan_name,
                ward_no=ward_project.ward_no
            ).exists()

            if already_exists:
                return Response({"error": "This project has already been prioritized."}, status=400)

            # Create prioritized entry
            PrioritizedWardLevelProject.objects.create(
                plan_name=ward_project.plan_name,
                thematic_area=ward_project.thematic_area,
                sub_area=ward_project.sub_area,
                source=ward_project.source,
                expenditure_center=ward_project.expenditure_center,
                budget=ward_project.budget,
                ward_no=ward_project.ward_no,
                status="प्राथमिकरण भएको वडा स्तरीय परियोजना",
                priority_no=ward_project.priority_no,
                remarks=ward_project.remarks
            )

            # Soft delete the original ward project
            ward_project.is_deleted = True
            ward_project.deleted_at = timezone.now()
            ward_project.save()

            return Response({"message": "Project prioritized and soft-deleted successfully."}, status=status.HTTP_200_OK)

        except WardLevelProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)


