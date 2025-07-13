from import_export import resources, fields
from projects.models.project import Project
from project_settings.models.thematic_area import ThematicArea
from project_settings.models.sub_thematic_area import SubArea
from project_settings.models.source import Source
from project_settings.models.expenditure_center import ExpenditureCenter
from project_settings.models.unit import Unit
from project_settings.models.fiscal_year import FiscalYear
from project_settings.models.project_level import ProjectLevel
from projects.my_widgets import SafeForeignKeyWidget 

class ProjectResource(resources.ModelResource):
    area = fields.Field(
        column_name='क्षेत्र',
        attribute='area',
        widget=SafeForeignKeyWidget(ThematicArea, 'name')
    )
    sub_area = fields.Field(
        column_name='उप-क्षेत्र',
        attribute='sub_area',
        widget=SafeForeignKeyWidget(SubArea, 'name')
    )
    source = fields.Field(
        column_name='स्रोत',
        attribute='source',
        widget=SafeForeignKeyWidget(Source, 'name')
    )
    expenditure_center = fields.Field(
        column_name='खर्च केन्द्र',
        attribute='expenditure_center',
        widget=SafeForeignKeyWidget(ExpenditureCenter, 'name')
    )
    project_level = fields.Field(
        column_name='Project Level',
        attribute='project_level',
        widget=SafeForeignKeyWidget(ProjectLevel, 'name')
    )
    fiscal_year = fields.Field(
        column_name='आर्थिक वर्ष',
        attribute='fiscal_year',
        widget=SafeForeignKeyWidget(FiscalYear, 'year')
    )
    unit = fields.Field(
        column_name='ईकाइ',
        attribute='unit',
        widget=SafeForeignKeyWidget(Unit, 'name')
    )

    class Meta:
        model = Project
        import_id_fields = ('project_name',)  # your unique field
        fields = (
            'serial_number', 'project_name', 'area', 'sub_area', 'source',
            'expenditure_center', 'project_level', 'budget', 'ward_no', 'status',
            'fiscal_year', 'location', 'location_gps', 'outcome', 'unit', 'is_active'
        )
        export_order = fields

