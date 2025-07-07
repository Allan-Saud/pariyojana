from dashboard.bar_graph.views import wardwise_budget_distribution
from dashboard.project_distribution.views import project_dashboard_summary
from django.urls import path
urlpatterns = [
    path('summary/', project_dashboard_summary, name='project-dashboard-summary'),
    path('wardwise-budget/', wardwise_budget_distribution, name='wardwise-budget'),
]
