from django.urls import path
from reports.views import ReportsDropdownsView,ExportReportExcelView

urlpatterns = [
    path('dropdowns/', ReportsDropdownsView.as_view(), name='reports-dropdowns'),
    path('export-excel/', ExportReportExcelView.as_view(), name='export-report-excel'),
]
