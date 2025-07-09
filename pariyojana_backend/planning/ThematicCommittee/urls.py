from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.ThematicCommittee.PlanEnteredByThematicCommittee.views import PlanEnteredByThematicCommitteeViewSet
from planning.ThematicCommittee.PrioritizedThematicCommittee.views import PrioritizedThematicCommitteeViewSet

router = DefaultRouter()
router.register(r'thematic-plans', PlanEnteredByThematicCommitteeViewSet,basename='thematic-plans')
# router.register(r'entered-plans', PlanEnteredByThematicCommitteeViewSet)
router.register(r'prioritized-plans', PrioritizedThematicCommitteeViewSet,basename='prioritized-plans')
# router.register(r'prioritized-thematic', PrioritizedThematicCommitteeViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
