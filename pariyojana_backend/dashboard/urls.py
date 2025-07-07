from dashboard.bar_graph.views import wardwise_budget_distribution
from dashboard.project_distribution.views import project_dashboard_summary
from dashboard.budget_expenditure.views import ProjectBudgetSummaryAPIView
from dashboard.Sum_Budget.views import AreaWiseProjectDistributionAPIView
from dashboard.Allocation_budget.views import budget_allocation_by_area
from django.urls import path
urlpatterns = [
    path('summary/', project_dashboard_summary, name='project-dashboard-summary'),
    path('wardwise-budget/', wardwise_budget_distribution, name='wardwise-budget'),
    path('budget-summary/', ProjectBudgetSummaryAPIView.as_view(), name='project-budget-summary'),
    path('area-wise-distribution/', AreaWiseProjectDistributionAPIView.as_view(), name='area-wise-distribution'),
    path('budget-area/', budget_allocation_by_area, name='budget-allocation-area'),
]
