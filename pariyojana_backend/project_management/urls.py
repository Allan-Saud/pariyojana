from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('user_auth.urls')),
    path('api/users/', include('users.urls')),
    path('api/settings/', include('project_settings.urls')),
    path('api/reports/', include('reports.urls')), 
    # path('api/', include('projects.urls')),
    path('api/projects/', include('projects.urls')),


]
