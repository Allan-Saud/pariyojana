from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models.project import Project

@api_view(['GET'])
def budget_allocation_by_area(request):
    projects_qs = Project.objects.filter(is_active=True, is_deleted=False)

    # Sum of budget grouped by area name
    area_budgets = projects_qs.values('area__name').annotate(total_budget=Sum('budget'))

    # Total budget sum across all projects (avoid division by zero)
    total_budget = projects_qs.aggregate(total=Sum('budget'))['total'] or 1

    result = []
    for item in area_budgets:
        percentage = (item['total_budget'] / total_budget) * 100
        result.append({
            'label': item['area__name'],
            'value': round(percentage, 2)
        })

    return Response(result)
