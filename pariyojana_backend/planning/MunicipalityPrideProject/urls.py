

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.MunicipalityPrideProject.views import MunicipalityPrideProjectViewSet
from planning.MunicipalityPrideProject.reports.enteredmunicipalityprideproject import EnteredMunicipalityprideProjectChart
from planning.MunicipalityPrideProject.reports.submittedprojectsTobudgetCommunity import SubmittedToBudgetMunicipalityPrideProjectChart
from planning.MunicipalityPrideProject.reports.submittedprojectsTobudgetCommunity import SubmittedToBudgetMunicipalityPrideProjectDownloadReport
from planning.MunicipalityPrideProject.reports.enteredmunicipalityprideproject import MunicipalityPrideProjectDownloadReport

router = DefaultRouter()
router.register('municipality-pride-projects', MunicipalityPrideProjectViewSet,basename='municipalprideproject')

urlpatterns = [
    path('', include(router.urls)),
    path('entered-municipality-chart/', EnteredMunicipalityprideProjectChart.as_view(), name='enteredmunicipality'),
    path('submitted-budget-chart/', SubmittedToBudgetMunicipalityPrideProjectChart.as_view(), name='submittedtobudget'),
    
    
    path('entered-municipality/report/', SubmittedToBudgetMunicipalityPrideProjectDownloadReport.as_view(), name='enteredmunicipalityreport'),
    path('submitted-budget/report/', SubmittedToBudgetMunicipalityPrideProjectDownloadReport.as_view(), name='submittedtobudgetreport'),
    
    
    
]
