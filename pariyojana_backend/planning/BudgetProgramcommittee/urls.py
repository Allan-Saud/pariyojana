from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.BudgetProgramcommittee.WardLevelProgram.views import BudgetProgramCommitteeWardLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.views import MunicipalityLevelProgramViewSet

router = DefaultRouter()

router.register(r'municipality-programs', MunicipalityLevelProgramViewSet)
router.register(r'budget-ward-projects', BudgetProgramCommitteeWardLevelProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
