from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from planning.WardOffice.WardLevelProject.models import WardLevelProject
from planning.WardOffice.PrioritizedWardLevelProjects.models import PrioritizedWardLevelProject
from planning.WardOffice.WardLevelProject.serializers import WardLevelProjectSerializer

class WardLevelProjectViewSet(viewsets.ModelViewSet):
    queryset = WardLevelProject.objects.all()
    serializer_class = WardLevelProjectSerializer

    @action(detail=True, methods=['post'], url_path='prioritize')
    def prioritize(self, request, pk=None):
        try:
            ward_project = self.get_object()
            priority_no = request.data.get('priority_no')
            if not priority_no:
                return Response({"error": "priority_no is required."}, status=400)

            PrioritizedWardLevelProject.objects.create(
                plan_name=ward_project.plan_name,
                thematic_area=ward_project.thematic_area,
                sub_area=ward_project.sub_area,
                source=ward_project.source,
                expenditure_center=ward_project.expenditure_center,
                budget=ward_project.budget,
                ward_no=ward_project.ward_no,
                status="प्राथमिकरण भएको वडा स्तरीय परियोजना",
                priority_no=priority_no,
                remarks=ward_project.remarks
            )
            ward_project.status = "प्राथमिकरण भएको वडा स्तरीय परियोजना"
            ward_project.priority_no = priority_no
            ward_project.save()

            return Response({"message": "Project prioritized successfully."}, status=status.HTTP_200_OK)

        except WardLevelProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
