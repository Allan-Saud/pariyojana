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
    serial_number = fields.Field(column_name='serial_number', attribute='serial_number', readonly=True)
    
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
        column_name='योजनाको स्तर',
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
    project_name = fields.Field(column_name='योजना तथा कार्यक्रम', attribute='project_name')
    budget = fields.Field(column_name='बजेट', attribute='budget')
    ward_no = fields.Field(column_name='वडा नंं', attribute='ward_no')
    status = fields.Field(column_name='स्थिती', attribute='status')
    location = fields.Field(column_name='योजना संचालन स्थान', attribute='location')
    location_gps = fields.Field(column_name='GPS समन्वय', attribute='location_gps')
    outcome = fields.Field(column_name='सम्पन्न गर्ने परिणाम', attribute='outcome')
    class Meta:
        model = Project
        import_id_fields = ('project_name',)  # or another unique field for updates
        fields = (
            'serial_number',  # included for export only (readonly)
            'project_name', 'area', 'sub_area', 'source',
            'expenditure_center', 'project_level', 'budget',
            'ward_no', 'status', 'fiscal_year',
            'location', 'location_gps', 'outcome', 'unit'
        )
        export_order = fields

    def before_import_row(self, row, **kwargs):
        fy_name = row.get('आर्थिक वर्ष')
        if fy_name:
            fiscal_year_obj, created = FiscalYear.objects.get_or_create(year=fy_name)
            row['fiscal_year'] = fiscal_year_obj.id

