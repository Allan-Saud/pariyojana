from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.BudgetProgramcommittee.WardLevelProgram.views import BudgetProgramCommitteeWardLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.views import MunicipalityLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityPrideProject.views import BudgetProgramMunicipalityPrideProgramViewSet
from planning.BudgetProgramcommittee.ProvinciallyTransferredProgram.views import ProvinciallyTransferredProgramViewSet
from planning.BudgetProgramcommittee.FederalGovernmentProject.views import BudgetProgramFederalGovernmentProgramViewSet
from planning.BudgetProgramcommittee.reports.MunicipalityLevelProgram import MunicipalityLevelProgramChart
from planning.BudgetProgramcommittee.reports.FederalGovernmentProject import BudgetProgramFederalGovernmentProgramChart
from planning.BudgetProgramcommittee.reports.MunicipalityPrideProject import BudgetProgramMunicipalityPrideProgramChart
from planning.BudgetProgramcommittee.reports.ProvinciallyTransferredProgram import ProvinciallyTransferredProgramChart
from planning.BudgetProgramcommittee.reports.ThematicCommitteeProgram import ThematicCommitteeProgramChart
from planning.BudgetProgramcommittee.reports.WardLevelProgram import BudgetProgramCommitteeWardLevelProgramChart




router = DefaultRouter()

router.register(r'municipality-programs', MunicipalityLevelProgramViewSet,basename='municipalityprograms')
router.register(r'municipality-pride', BudgetProgramMunicipalityPrideProgramViewSet,basename='municipalitypride')
router.register(r'budget-ward-projects', BudgetProgramCommitteeWardLevelProgramViewSet, basename='budgetwardproject')
router.register(r'provience-transfer-projects', ProvinciallyTransferredProgramViewSet, basename='proviencetransfer')
router.register(r'federal-gov-projects', BudgetProgramFederalGovernmentProgramViewSet, basename='federalgov')




urlpatterns = [
    path('', include(router.urls)),
    path('municipalitylevel-chart/', MunicipalityLevelProgramChart.as_view(), name='municipalitylevelchart'),
    path('federalgov-chart/', BudgetProgramFederalGovernmentProgramChart.as_view(), name='federalgovchart'),
    path('municipalitypride-chart/', BudgetProgramMunicipalityPrideProgramChart.as_view(), name='municipalitypridechart'),
    path('provinciallytransfer-chart/', ProvinciallyTransferredProgramChart.as_view(), name='provinciallytransferchart'),
    path('thematiccommittee-chart/', ThematicCommitteeProgramChart.as_view(), name='thematiccommitteechart'),
    path('wardlevel-chart/', BudgetProgramCommitteeWardLevelProgramChart.as_view(), name='wardlevelchart'),
    
]
