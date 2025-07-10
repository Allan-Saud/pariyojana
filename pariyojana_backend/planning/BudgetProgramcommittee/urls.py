from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.BudgetProgramcommittee.WardLevelProgram.views import BudgetProgramCommitteeWardLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.views import MunicipalityLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityPrideProject.views import BudgetProgramMunicipalityPrideProgramViewSet
from planning.BudgetProgramcommittee.ProvinciallyTransferredProgram.views import ProvinciallyTransferredProgramViewSet
from planning.BudgetProgramcommittee.FederalGovernmentProject.views import BudgetProgramFederalGovernmentProgramViewSet


router = DefaultRouter()

router.register(r'municipality-programs', MunicipalityLevelProgramViewSet,basename='municipalityprograms')
router.register(r'municipality-pride', BudgetProgramMunicipalityPrideProgramViewSet,basename='municipalitypride')
router.register(r'budget-ward-projects', BudgetProgramCommitteeWardLevelProgramViewSet, basename='budgetwardproject')
router.register(r'provience-transfer-projects', ProvinciallyTransferredProgramViewSet, basename='proviencetransfer')
router.register(r'federal-gov-projects', BudgetProgramFederalGovernmentProgramViewSet, basename='federalgov')




urlpatterns = [
    path('', include(router.urls)),
]
