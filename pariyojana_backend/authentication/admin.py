from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Customize how Users are displayed in Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'role', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'phone', 'ward_no')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active')}),
    )
    ordering = ['email']  
