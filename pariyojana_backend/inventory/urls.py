
from rest_framework.routers import DefaultRouter
from .views import SupplierRegistryViewSet
from django.urls import path, include
from inventory.views import inventory_pdf_view
router = DefaultRouter()
router.register(r'supplier-registry', SupplierRegistryViewSet, basename='supplier-registry')
from django.conf import settings
from django.conf.urls.static import static
# urlpatterns = [
#     path('', include(router.urls)),
#     path("inventory-report/", inventory_pdf_view, name="inventory_pdf"),
# ]




urlpatterns = [
    path('', include(router.urls)),
    path("inventory-report/", inventory_pdf_view, name="inventory_pdf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
