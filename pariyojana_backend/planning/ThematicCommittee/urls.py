from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.ThematicCommittee.PlanEnteredByThematicCommittee.views import PlanEnteredByThematicCommitteeViewSet
from planning.ThematicCommittee.PrioritizedThematicCommittee.views import PrioritizedThematicCommitteeViewSet
from planning.ThematicCommittee.WardRecommendedProjects.views import WardRecommendedProjectsViewSet
from planning.ThematicCommittee.reports.prioritizedthemantic import PrioritizedWardThematicChartData
from planning.ThematicCommittee.reports.planenteredthemantic import PlanEnteredByThematicCommitteeChartData
from planning.ThematicCommittee.reports.wardrecommended import WardrecommendetChart




router = DefaultRouter()
router.register(r'thematic-plans', PlanEnteredByThematicCommitteeViewSet,basename='thematic-plans')
# router.register(r'entered-plans', PlanEnteredByThematicCommitteeViewSet)
router.register(r'prioritized-plans', PrioritizedThematicCommitteeViewSet,basename='prioritized-plans')
router.register(r'wardrecommend-project', WardRecommendedProjectsViewSet,basename='ward-plans')

# router.register(r'prioritized-thematic', PrioritizedThematicCommitteeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('wardlevel-chart/', PlanEnteredByThematicCommitteeChartData.as_view(), name='wardlevelchart'),
    path('wardlevelthemtic-chart/', PrioritizedWardThematicChartData.as_view(), name='wardlevelthematicchart'),
    path('Wardrecommended-chart/', WardrecommendetChart.as_view(), name='municipalitylevelchart'),
    
]
