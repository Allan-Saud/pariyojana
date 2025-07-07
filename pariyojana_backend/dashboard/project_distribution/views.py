# views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from projects.models.project import Project

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def project_dashboard_summary(request):
    total_projects = Project.objects.filter(is_deleted=False).count()
    completed_projects = Project.objects.filter(status='completed', is_deleted=False).count()
    not_started_projects = Project.objects.filter(status='not_started', is_deleted=False).count()
    in_progress_projects = Project.objects.filter(status='process_ensured', is_deleted=False).count()

    return Response({
        "total_projects": total_projects,
        "completed_projects": completed_projects,
        "not_started_projects": not_started_projects,
        "in_progress_projects": in_progress_projects
    })
