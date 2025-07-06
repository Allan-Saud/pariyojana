from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from projects.models.project import Project
from projects.models.Program_Details.program_detail import ProgramDetail
from projects.serializers.Program_Details.program_detail import ProgramDetailSerializer
from rest_framework import viewsets
from projects.serializers.project import ProjectSerializer


# class ProgramDetailViewSet(viewsets.ModelViewSet):
#     queryset = ProgramDetail.objects.all()
#     serializer_class = ProgramDetailSerializer
class ProgramDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramDetailSerializer

    def get_queryset(self):
        queryset = ProgramDetail.objects.all()
        project_id = self.request.query_params.get('project_id')  

        if project_id:
            queryset = queryset.filter(project__serial_number=project_id)

        return queryset

    @action(detail=False, methods=['post'], url_path='create-from-project')
    def create_from_project(self, request):
        """
        Create ProgramDetail from a given project serial_number.
        """
        serial_number = request.data.get('serial_number')
        if not serial_number:
            return Response({'error': 'serial_number is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            project = Project.objects.get(serial_number=serial_number)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        program_detail_data = {
            'project': project.serial_number,
            'project_name': project.project_name,
            'ward_no': project.ward_no,
            'fiscal_year': project.fiscal_year.id if project.fiscal_year else None,
            'area': project.area.id if project.area else None,
            'sub_area': project.sub_area.id if project.sub_area else None,
            'source': project.source.id if project.source else None,
            'expenditure_center': project.expenditure_center.id if project.expenditure_center else None,
            'outcome': project.outcome,
            'budget': project.budget,
            'location_gps': project.location_gps,
            'status': project.status,
            'project_level':project.project_level
        }

        serializer = self.get_serializer(data=program_detail_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'], url_path='project-details/(?P<project_id>[^/.]+)')
    def get_project_details(self, request, project_id=None):
        try:
            project = Project.objects.get(serial_number=project_id)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=404)

        serializer = ProjectSerializer(project)
        return Response(serializer.data)
