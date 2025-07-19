from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from projects.models.project import Project
from projects.serializers.project import ProjectSerializer
from django.utils import timezone
import tablib
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser 
from projects.resources import ProjectResource
from django.http import HttpResponse
from tablib import Dataset

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.filter(is_deleted=False)
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save()

#     def perform_update(self, serializer):
#         serializer.save()

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.is_deleted = True
#         instance.is_active = False
#         instance.deleted_at = timezone.now()
#         instance.deleted_by = request.user
#         instance.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_deleted=False)
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser] 

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.is_active = False
        instance.deleted_at = timezone.now()
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def export(self, request):
        resource = ProjectResource()

       
        dataset = Dataset(headers=resource.get_export_headers())

        response = HttpResponse(
            dataset.export('xlsx'),  
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="projects_template.xlsx"'
        return response

    @action(detail=False, methods=['post'])
    def import_excel(self, request):
        resource = ProjectResource()
        dataset = tablib.Dataset()
        new_projects = request.FILES.get('file')

        if not new_projects:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            imported_data = tablib.Dataset().load(new_projects.read(), format='xlsx')
        except Exception as e:
            return Response({'error': f'Invalid file format: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        result = resource.import_data(imported_data, dry_run=True)  

        if result.has_errors():
            return Response({'error': 'Import errors', 'details': str(result.row_errors())}, status=status.HTTP_400_BAD_REQUEST)

        resource.import_data(imported_data, dry_run=False) 

        return Response({'success': 'Projects imported successfully'}, status=status.HTTP_200_OK)

