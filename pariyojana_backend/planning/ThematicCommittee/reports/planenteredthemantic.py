from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from planning.ThematicCommittee.PlanEnteredByThematicCommittee.models import PlanEnteredByThematicCommittee


class PPlanEnteredByThematicCommitteeChartData(APIView):
    def get(self, request):
        # Get all non-deleted entries
        projects = PlanEnteredByThematicCommittee.objects.filter(is_deleted=False)

        # 1. Sector-wise Budget Distribution
        budget_data = (
            projects.values('thematic_area__name')
            .annotate(total_budget=Sum('budget'))
            .order_by('-total_budget')
        )

        total_budget = sum(item['total_budget'] for item in budget_data)

        budget_chart = [
            {
                'label': item['thematic_area__name'],
                'value': float(item['total_budget']),
                'percentage': round((item['total_budget'] / total_budget) * 100, 2) if total_budget > 0 else 0
            }
            for item in budget_data
        ]

        # 2. Sector-wise Project Count
        count_data = (
            projects.values('thematic_area__name')
            .annotate(project_count=Count('id'))
            .order_by('-project_count')
        )

        total_projects = sum(item['project_count'] for item in count_data)

        count_chart = [
            {
                'label': item['thematic_area__name'],
                'value': item['project_count'],
                'percentage': round((item['project_count'] / total_projects) * 100, 2) if total_projects > 0 else 0
            }
            for item in count_data
        ]

        return Response({
            'budget_distribution': budget_chart,
            'project_count_distribution': count_chart
        })
