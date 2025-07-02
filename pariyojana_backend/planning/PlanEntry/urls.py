from rest_framework.routers import DefaultRouter
from planning.PlanEntry.views import PlanEntryViewSet

router = DefaultRouter()
router.register(r'plan-entry', PlanEntryViewSet, basename='plan-entry')

urlpatterns = router.urls
