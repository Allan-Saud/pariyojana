# from rest_framework import viewsets, status
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework.decorators import action
from projects.models.Consumer_Committee.official_detail import OfficialDetail
# from projects.serializers.Consumer_Committee.official_detail import OfficialDetailSerializer
from projects.serializers.Consumer_Committee.official_detail import (
    OfficialDetailSerializer,
    OfficialDetailCreateUpdateSerializer,
    OfficialDetailListSerializer
)

from projects.models.project import Project
# from django.shortcuts import get_object_or_404
# from django.db import models
# from collections import defaultdict

# class OfficialDetailViewSet(viewsets.ViewSet):
#     parser_classes = [MultiPartParser, FormParser]

#     def list(self, request, serial_number=None):
#         queryset = OfficialDetail.objects.filter(project__serial_number=serial_number).order_by('serial_no')
#         serializer = OfficialDetailSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request, serial_number=None):
#         project = get_object_or_404(Project, serial_number=serial_number)

#         # Get max serial_no for this project
#         max_serial = OfficialDetail.objects.filter(project=project).aggregate(models.Max('serial_no'))['serial_no__max']
#         next_serial_no = (max_serial or 0) + 1  # if none, start with 1

#         serializer = OfficialDetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(project=project, serial_no=next_serial_no)  # pass serial_no explicitly
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     @action(detail=False, methods=['patch'], url_path='bulk-update')
#     def bulk_update_by_serial(self, request, serial_number=None):
#         project = get_object_or_404(Project, serial_number=serial_number)

#         serial_no = request.data.get('serial_no')
#         if not serial_no:
#             return Response({'error': 'serial_no is required.'}, status=400)

#         try:
#             official = OfficialDetail.objects.get(project=project, serial_no=serial_no)
#             serializer = OfficialDetailSerializer(official, data=request.data, partial=True)
#         except OfficialDetail.DoesNotExist:
#             # Create new if not exists
#             # serializer = OfficialDetailSerializer(data={**request.data, 'project': project.id, 'serial_no': serial_no})
#             serializer = OfficialDetailSerializer(data={**request.data, 'project': project.serial_number, 'serial_no': serial_no})


#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         else:
#             return Response(serializer.errors, status=400)


# projects/views/official_detail.py

from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.db import transaction


class OfficialDetailListCreateView(generics.ListCreateAPIView):
    """
    List all officials for a project or create a new official
    """
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_serial = self.kwargs['project_id']
        return OfficialDetail.objects.filter(project__serial_number=project_serial).order_by('serial_no')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OfficialDetailCreateUpdateSerializer
        return OfficialDetailListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        project_serial = self.kwargs['project_id']
        project = get_object_or_404(Project, serial_number=project_serial)
        context['project'] = project
        return context

    def perform_create(self, serializer):
        project_serial = self.kwargs['project_id']
        project = get_object_or_404(Project, serial_number=project_serial)
        serializer.save(project=project)

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class OfficialDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an official
    """
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_serial = self.kwargs['project_id']
        return OfficialDetail.objects.filter(project__serial_number=project_serial)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return OfficialDetailCreateUpdateSerializer
        return OfficialDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        project_serial = self.kwargs['project_id']
        project = get_object_or_404(Project, serial_number=project_serial)
        context['project'] = project
        return context

    def update(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_official_choices(request, project_id):
    """
    Get available choices for form fields
    """
    project = get_object_or_404(Project, serial_number=project_id)

    choices = {
        'post_choices': OfficialDetail.POST_CHOICES,
        'gender_choices': OfficialDetail.GENDER_CHOICES,
    }

    return Response(choices)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bulk_create_officials(request, project_id):
    """
    Create multiple officials at once
    """
    project = get_object_or_404(Project, serial_number=project_id)

    officials_data = request.data.get('officials', [])
    if not officials_data:
        return Response(
            {'error': 'No officials data provided'},
            status=status.HTTP_400_BAD_REQUEST
        )

    created_officials = []
    errors = []

    try:
        with transaction.atomic():
            for idx, official_data in enumerate(officials_data):
                serializer = OfficialDetailCreateUpdateSerializer(
                    data=official_data,
                    context={'project': project, 'request': request}
                )

                if serializer.is_valid():
                    official = serializer.save(project=project)
                    created_officials.append(
                        OfficialDetailSerializer(official, context={'request': request}).data
                    )
                else:
                    errors.append({
                        'index': idx,
                        'errors': serializer.errors
                    })

            if errors:
                return Response(
                    {'errors': errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({
        'message': f'Successfully created {len(created_officials)} officials',
        'officials': created_officials
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_next_serial_number(request, project_id):
    """
    Get the next available serial number for the project
    """
    project = get_object_or_404(Project, serial_number=project_id)

    last_official = OfficialDetail.objects.filter(
        project=project
    ).order_by('-serial_no').first()

    next_serial = 1 if not last_official else last_official.serial_no + 1

    return Response({'next_serial_no': next_serial})


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def reorder_officials(request, project_id):
    """
    Reorder officials by updating their serial numbers
    """
    project = get_object_or_404(Project, serial_number=project_id)

    official_orders = request.data.get('orders', [])
    # Expected format: [{'id': 1, 'serial_no': 1}, {'id': 2, 'serial_no': 2}, ...]

    if not official_orders:
        return Response(
            {'error': 'No order data provided'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        with transaction.atomic():
            for order_data in official_orders:
                official_id = order_data.get('id')
                new_serial_no = order_data.get('serial_no')

                if not official_id or new_serial_no is None:
                    continue

                OfficialDetail.objects.filter(
                    id=official_id,
                    project=project
                ).update(serial_no=new_serial_no)

        # Return updated list
        officials = OfficialDetail.objects.filter(
            project=project
        ).order_by('serial_no')

        serializer = OfficialDetailListSerializer(
            officials,
            many=True,
            context={'request': request}
        )

        return Response({
            'message': 'Officials reordered successfully',
            'officials': serializer.data
        })

    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )


