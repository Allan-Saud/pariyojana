from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.BudgetProgramcommittee.WardLevelProgram.views import BudgetProgramCommitteeWardLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityLevelProgram.views import MunicipalityLevelProgramViewSet
from planning.BudgetProgramcommittee.MunicipalityPrideProject.views import BudgetProgramMunicipalityPrideProgramViewSet
from planning.BudgetProgramcommittee.ProvinciallyTransferredProgram.views import ProvinciallyTransferredProgramViewSet
from planning.BudgetProgramcommittee.FederalGovernmentProject.views import BudgetProgramFederalGovernmentProgramViewSet
from planning.BudgetProgramcommittee.ThematicCommitteeProgram.views import ThematicCommitteeProgramViewSet

from planning.BudgetProgramcommittee.reports.MunicipalityLevelProgram import MunicipalityLevelProgramChart
from planning.BudgetProgramcommittee.reports.FederalGovernmentProject import BudgetProgramFederalGovernmentProgramChart
from planning.BudgetProgramcommittee.reports.MunicipalityPrideProject import BudgetProgramMunicipalityPrideProgramChart
from planning.BudgetProgramcommittee.reports.ProvinciallyTransferredProgram import ProvinciallyTransferredProgramChart
from planning.BudgetProgramcommittee.reports.ThematicCommitteeProgram import ThematicCommitteeProgramChart
from planning.BudgetProgramcommittee.reports.WardLevelProgram import BudgetProgramCommitteeWardLevelProgramChart

from planning.BudgetProgramcommittee.reports.ProvinciallyTransferredProgram import ProvinciallytransferredProgramDownloadReport
from planning.BudgetProgramcommittee.reports.FederalGovernmentProject import BudgetProgramFederalGovernmentProgramDownloadReport
from planning.BudgetProgramcommittee.reports.MunicipalityLevelProgram import MunicipalityLevelProgramDownloadReport
from planning.BudgetProgramcommittee.reports.MunicipalityPrideProject import BudgetProgramMunicipalityPrideProgramDownloadReport
from planning.BudgetProgramcommittee.reports.ThematicCommitteeProgram import ThematicCommitteeProgramDownloadReport
from planning.BudgetProgramcommittee.reports.WardLevelProgram import BudgetProgramCommitteeWardLevelProgramDownloadReport






router = DefaultRouter()

router.register(r'municipality-programs', MunicipalityLevelProgramViewSet,basename='municipalityprograms')
router.register(r'municipality-pride', BudgetProgramMunicipalityPrideProgramViewSet,basename='municipalitypride')
router.register(r'budget-ward-projects', BudgetProgramCommitteeWardLevelProgramViewSet, basename='budgetwardproject')
router.register(r'provience-transfer-projects', ProvinciallyTransferredProgramViewSet, basename='proviencetransfer')
router.register(r'federal-gov-projects', BudgetProgramFederalGovernmentProgramViewSet, basename='federalgov')
router.register(r'thematic-committee', ThematicCommitteeProgramViewSet, basename='thematiccommittee')





urlpatterns = [
    path('', include(router.urls)),
    path('municipalitylevel-chart/', MunicipalityLevelProgramChart.as_view(), name='municipalitylevelchart'),
    path('federalgov-chart/', BudgetProgramFederalGovernmentProgramChart.as_view(), name='federalgovchart'),
    path('municipalitypride-chart/', BudgetProgramMunicipalityPrideProgramChart.as_view(), name='municipalitypridechart'),
    path('provinciallytransfer-chart/', ProvinciallyTransferredProgramChart.as_view(), name='provinciallytransferchart'),
    path('thematiccommittee-chart/', ThematicCommitteeProgramChart.as_view(), name='thematiccommitteechart'),
    path('wardlevel-chart/', BudgetProgramCommitteeWardLevelProgramChart.as_view(), name='wardlevelchart'),
    
    
    
    path('municipalitylevel/report/', MunicipalityLevelProgramDownloadReport.as_view(), name='municipalitylevel'),
    path('federalgov/report/', BudgetProgramFederalGovernmentProgramDownloadReport.as_view(), name='federalgov'),
    path('municipalitypride/report/', BudgetProgramMunicipalityPrideProgramDownloadReport.as_view(), name='municipalitypride'),
    path('provinciallytransfer/report/', ProvinciallytransferredProgramDownloadReport.as_view(), name='provinciallytransfer'),
    path('thematiccommittee/report/', ThematicCommitteeProgramDownloadReport.as_view(), name='thematiccommitte'),
    path('wardlevel/report/', BudgetProgramCommitteeWardLevelProgramDownloadReport.as_view(), name='wardlevel'),
    
]
