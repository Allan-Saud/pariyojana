from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from projects.models.project import Project

class AreaWiseProjectDistributionAPIView(APIView):
    def get(self, request):
        # Filter active projects
        projects_qs = Project.objects.filter(is_active=True, is_deleted=False)
        total_projects = projects_qs.count()

        # Aggregate counts grouped by area name
        area_counts = projects_qs.values('area__name').annotate(count=Count('serial_number'))
        # Prepare response data with percentages
        result = []
        for item in area_counts:
            percentage = (item['count'] / total_projects) * 100 if total_projects else 0
            result.append({
                "label": item['area__name'],
                "value": round(percentage, 2)
            })

        return Response(result)
