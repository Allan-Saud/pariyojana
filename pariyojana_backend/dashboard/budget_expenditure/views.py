from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from projects.models.project import Project
from projects.models.Installment_Payment.payment_related_details import PaymentRelatedDetail

class ProjectBudgetSummaryAPIView(APIView):
    def get(self, request):
        # Sum budget from all active, not deleted projects
        total_budget = Project.objects.filter(is_active=True, is_deleted=False).aggregate(
            total=Sum('budget')
        )['total'] or 0

        # Sum paid amounts from all active payment details linked to active projects
        expenditure = PaymentRelatedDetail.objects.filter(
            is_active=True,
            project__is_active=True,
            project__is_deleted=False,
        ).aggregate(total=Sum('amount_paid'))['total'] or 0

        remaining = total_budget - expenditure

        return Response({
            "total_budget": total_budget,
            "expenditure_budget": expenditure,
            "remaining_budget": remaining,
        })
