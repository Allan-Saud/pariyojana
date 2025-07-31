from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from projects.models.project import Project
from django.db.models import Sum

# @api_view(['GET'])
# @permission_classes([IsAuthenticated]) 
# def wardwise_budget_distribution(request):
#     result = (
#         Project.objects
#         .filter(is_deleted=False)
#         .values('ward_no')
#         .annotate(total_budget=Sum('budget'))
#         .order_by('ward_no')
#     )

#     return Response(result)


from django.db.models import Sum, F
from django.db.models.expressions import Func, Value
from django.db.models.fields import IntegerField
from django.db.models import OuterRef, Subquery

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def wardwise_budget_distribution(request):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT unnest(ward_no) AS ward, SUM(budget) AS total_budget
            FROM projects_project
            WHERE is_deleted = FALSE
            GROUP BY ward
            ORDER BY ward;
        """)
        rows = cursor.fetchall()

    # Format response as list of dicts
    result = [{"ward_no": row[0], "total_budget": float(row[1])} for row in rows]
    return Response(result)

