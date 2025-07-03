from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planning.PlanEntry.views import PlanEntryViewSet

router = DefaultRouter()
router.register(r'plan-entry', PlanEntryViewSet, basename='plan-entry')


urlpatterns = [
    path('', include(router.urls)),
    path('ward-office/', include('planning.WardOffice.urls')),
    path('budget-committee/', include('planning.BudgetProgramcommittee.urls')),
    path('municipality-executive/', include('planning.MunicipalityExecutiveOffice.PreAssemblyProject.urls')),
    path('municipal-assembly/', include('planning.MunicipalAssembly.SubmittedProjects.urls')),
    path('municipal-assembly-edit/', include('planning.MunicipalAssembly.ProjectsApprovedByMunicipal.urls')),




]
