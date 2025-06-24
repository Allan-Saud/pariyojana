from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project_settings.views.thematic_area import ThematicAreaViewSet
from project_settings.views.sub_thematic_area import SubAreaViewSet
from project_settings.views.group import GroupViewSet
from project_settings.views.project_level import ProjectLevelViewSet
from project_settings.views.expenditure_title import ExpenditureTitleViewSet
from project_settings.views.expenditure_center import ExpenditureCenterViewSet
from project_settings.views.source import SourceViewSet
from project_settings.views.unit import UnitViewSet
from project_settings.views.pride_project_title import PrideProjectTitleViewSet
from project_settings.views.fiscal_year import FiscalYearViewSet
from project_settings.views.bank import BankViewSet
from project_settings.views.template import TemplateViewSet

router = DefaultRouter()
router.register(r'thematic-area', ThematicAreaViewSet, basename='thematic-area')
router.register(r'sub-thematic-area', SubAreaViewSet, basename='sub-thematic-area')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'project-level', ProjectLevelViewSet, basename='project-level')
router.register(r'expenditure-title', ExpenditureTitleViewSet, basename='expenditure-title')
router.register(r'expenditure-center', ExpenditureCenterViewSet, basename='expenditure-center')
router.register(r'source', SourceViewSet, basename='source')
router.register(r'unit', UnitViewSet, basename='unit')
router.register(r'pride-project-title', PrideProjectTitleViewSet, basename='pride-project-title')
router.register(r'fiscal-year', FiscalYearViewSet, basename='fiscal-year')
router.register(r'bank', BankViewSet, basename='bank')
router.register(r'template', TemplateViewSet, basename='template')

urlpatterns = [
    path('', include(router.urls)),
]



# विषयगत क्षेत्र = Thematic Area
# उप-क्षेत्र = Sub‑Area
# समूह = Group
# योजनाको स्तर = Project Level
# खर्च शीर्षक = Expenditure Head (Title)
# खर्च केन्द्र = Expenditure Centre
# स्रोत = Source
# इकाई = Unit
# नगर गौरव योजनाको शीर्षक = Municipal “Pride Project” Title
# आर्थिक वर्ष = Fiscal Year
# बैंकहरू = (Project) Banks / Project Database
# नमूनाहरु = templates
