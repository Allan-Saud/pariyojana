from django.contrib import admin
from .models.project import Project
from projects.models.Initiation_Process.initiation_process import InitiationProcess
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate

# Inline for documents
class MapCostEstimateInline(admin.TabularInline):
    model = MapCostEstimate
    extra = 1
    fields = ('title', 'status', 'checker', 'approver', 'is_verified')

# Inline for initiation process
class InitiationProcessInline(admin.StackedInline):
    model = InitiationProcess
    extra = 1
    fields = ('initiation_method', 'is_confirmed', 'started_at')

# Main Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'project_name', 'status', 'ward_no', 'budget')
    inlines = [InitiationProcessInline, MapCostEstimateInline]

# Document Admin (separate view)
@admin.register(MapCostEstimate)
class MapCostEstimateAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'checker', 'approver')