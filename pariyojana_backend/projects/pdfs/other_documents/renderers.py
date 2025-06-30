from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def render_pdf(template_path, context, output_filename):
    template = get_template(template_path)
    html = template.render(context)
    result = BytesIO()
    status = pisa.CreatePDF(html, dest=result)

    if status.err:
        return None, None

    return result.getvalue(), output_filename
