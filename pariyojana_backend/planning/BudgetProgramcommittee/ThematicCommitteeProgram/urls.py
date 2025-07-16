# planning/BudgetProgramcommittee/ThematicCommitteeProgram/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThematicCommitteeProgramViewSet

router = DefaultRouter()
router.register(r'thematic-programs', ThematicCommitteeProgramViewSet,basename='thematic-program')
# router.register(r'thematic-programs', ThematicCommitteeProgramViewSet, basename='thematic-program')

urlpatterns = [
    path('', include(router.urls)),
]
