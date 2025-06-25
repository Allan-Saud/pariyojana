# reports/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Thematic Area
from project_settings.models.thematic_area import ThematicArea
from project_settings.serializers.thematic_area import ThematicAreaSerializer

# Additional Imports
from project_settings.models.sub_thematic_area import SubArea
from project_settings.serializers.sub_thematic_area import SubAreaSerializer

from project_settings.models.source import Source
from project_settings.serializers.source import SourceSerializer

from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.serializers.expenditure_center import ExpenditureCenterSerializer

from project_settings.models.fiscal_year import FiscalYear
from project_settings.serializers.fiscal_year import FiscalYearSerializer

import openpyxl
from openpyxl.utils import get_column_letter
from django.http import HttpResponse


class ReportsDropdownsView(APIView):
    def get(self, request):
        # Hardcoded values
        report_types = [
            "सम्पन्न नभएको परियोजनाहरू",
            "परियोजना अनुसार बजेट",
            "प्रगति रिपोर्ट"
        ]
        statuses = [
            "सञ्‍चालित",
            "सम्पन्न भएको",
            "सुचारु प्रक्रिया सुनिस्चित भएको",
            "सुरु नभएको"
        ]
        wards = [f"वडा नं.-{i}" for i in range(1, 9)]

        # Dynamic values
        thematic_areas = ThematicAreaSerializer(ThematicArea.objects.filter(is_active=True), many=True).data
        sub_areas = SubAreaSerializer(SubArea.objects.filter(is_active=True), many=True).data
        sources = SourceSerializer(Source.objects.filter(is_active=True), many=True).data
        expenditure_centers = ExpenditureCenterSerializer(ExpenditureCenter.objects.filter(is_active=True), many=True).data
        fiscal_years = FiscalYearSerializer(FiscalYear.objects.all(), many=True).data

        return Response({
            "report_types": report_types,
            "statuses": statuses,
            "wards": wards,
            "thematic_areas": thematic_areas,
            "sub_areas": sub_areas,
            "sources": sources,
            "expenditure_centers": expenditure_centers,
            "fiscal_years": fiscal_years,
        }, status=status.HTTP_200_OK)


class ExportReportExcelView(APIView):
    def get(self, request):
        # You can receive filters from query parameters like:
        report_type = request.query_params.get('report_type')
        ward = request.query_params.get('ward')
        status = request.query_params.get('status')

        # Replace this with real DB data later based on filters
        data = [
            ['Project Name', 'Ward No.', 'Status', 'Thematic Area'],
            ['Water Supply', 'वडा नं.-1', 'सञ्‍चालित', 'शिक्षा'],
            ['Drainage Project', 'वडा नं.-3', 'सम्पन्न भएको', 'पुर्वाधार'],
        ]

        # Create Excel workbook
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Report"

        for row in data:
            ws.append(row)

        # Optional: auto column width
        for col in ws.columns:
            max_length = 0
            column = get_column_letter(col[0].column)
            for cell in col:
                if cell.value and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            ws.column_dimensions[column].width = max_length + 2

        # Send as response
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        wb.save(response)
        return response