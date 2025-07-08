from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.BudgetProgramcommittee.WardLevelProgram.views import BudgetProgramCommitteeWardLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.views import MunicipalityLevelProgramViewSet

router = DefaultRouter()

router.register(r'municipality-programs', MunicipalityLevelProgramViewSet,basename='municipalityprograms')
# router.register(r'budget-ward-projects', BudgetProgramCommitteeWardLevelProgramViewSet)
router.register(r'budget-ward-projects', BudgetProgramCommitteeWardLevelProgramViewSet, basename='budgetwardproject')


urlpatterns = [
    path('', include(router.urls)),
]
