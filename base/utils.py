from io import BytesIO

from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict):
    result = BytesIO()
    template = render_to_string(template_src, context_dict)
    pdf = pisa.pisaDocument(BytesIO(template.encode('UTF-8')), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return None
