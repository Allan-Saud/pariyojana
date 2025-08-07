# views/supplier_registry.py
from rest_framework import viewsets, permissions
from .models import SupplierRegistry
from .serializers import SupplierRegistrySerializer
from rest_framework.parsers import MultiPartParser, FormParser

class SupplierRegistryViewSet(viewsets.ModelViewSet):
    queryset = SupplierRegistry.objects.all().order_by('-created_at')
    serializer_class = SupplierRegistrySerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)




from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings
from inventory.models import SupplierRegistry

def inventory_pdf_view(request):
    items = SupplierRegistry.objects.all()

    html_string = render_to_string("inventory/inventory.html", {
        "items": items
    })

#    html_string = render_to_string('inventory/application_form.html', context)

    # Create a PDF from HTML
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf_file = html.write_pdf()

    # Return as downloadable response
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inventory.pdf"'
    return response
