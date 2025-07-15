# # projects/views/official_detail.py

# from rest_framework import viewsets
# from rest_framework.parsers import MultiPartParser, FormParser
# from projects.models.Consumer_Committee.official_detail import OfficialDetail
# from projects.serializers.Consumer_Committee.official_detail import OfficialDetailSerializer
# from projects.models.project import Project

# class OfficialDetailViewSet(viewsets.ModelViewSet):
#     queryset = OfficialDetail.objects.all().order_by('serial_no')
#     serializer_class = OfficialDetailSerializer
#     parser_classes = [MultiPartParser, FormParser]

#     def get_queryset(self):
#         queryset = super().get_queryset().order_by('serial_no')

#         # Support nested route: /projects/<serial_number>/official-details/
#         serial_number = self.kwargs.get('serial_number')
#         if serial_number:
#             queryset = queryset.filter(project__serial_number=serial_number)

#         # Also support query param: ?project=6
#         query_param = self.request.query_params.get('project')
#         if query_param:
#             queryset = queryset.filter(project__serial_number=query_param)

#         return queryset

    
#     def perform_create(self, serializer):
#         project_sn = self.request.query_params.get('project')
#         if not project_sn:
#             raise Exception("Project ID (serial_number) is required in query parameters.")

#         try:
#             project = Project.objects.get(serial_number=project_sn)
#         except Project.DoesNotExist:
#             raise Exception(f"Project with serial_number={project_sn} not found.")

#         serializer.save(project=project)


from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from projects.models.Consumer_Committee.official_detail import OfficialDetail
from projects.serializers.Consumer_Committee.official_detail import OfficialDetailSerializer
from projects.models.project import Project
from django.shortcuts import get_object_or_404
from django.db import models
from collections import defaultdict

class OfficialDetailViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, FormParser]

    def list(self, request, serial_number=None):
        queryset = OfficialDetail.objects.filter(project__serial_number=serial_number).order_by('serial_no')
        serializer = OfficialDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request, serial_number=None):
    #     project = get_object_or_404(Project, serial_number=serial_number)
    #     serializer = OfficialDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(project=project)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, serial_number=None):
        project = get_object_or_404(Project, serial_number=serial_number)

        # Get max serial_no for this project
        max_serial = OfficialDetail.objects.filter(project=project).aggregate(models.Max('serial_no'))['serial_no__max']
        next_serial_no = (max_serial or 0) + 1  # if none, start with 1

        serializer = OfficialDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project=project, serial_no=next_serial_no)  # pass serial_no explicitly
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['patch'], url_path='bulk-update')
    def bulk_update_by_serial(self, request, serial_number=None):
        project = get_object_or_404(Project, serial_number=serial_number)

        serial_no = request.data.get('serial_no')
        if not serial_no:
            return Response({'error': 'serial_no is required.'}, status=400)

        try:
            official = OfficialDetail.objects.get(project=project, serial_no=serial_no)
            serializer = OfficialDetailSerializer(official, data=request.data, partial=True)
        except OfficialDetail.DoesNotExist:
            # Create new if not exists
            serializer = OfficialDetailSerializer(data={**request.data, 'project': project.id, 'serial_no': serial_no})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)





