from .models import Mijoz
# from io import BytesIO
from io import BytesIO
from tempfile import template
from unittest import result
from .filter import KassaFilter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# import reportlab
# import io
# from django.http import FileResponse, HttpResponse
# from reportlab.pdfgen import canvas
# # from django.utils.safestring import SafeData
# from xhtml2pdf import pisa
from datetime import datetime
from .models import Mijoz, Sklad, Category, ishch, sotibol, kassa, Tranzaksiya, sharnoma, sotilgan
from .form import SkladForm, CategoryForm, ishchiForm, MijozForm, sotibolForm, sotilganForm, TranzaksiyaForm, kassaForm
from django.http import HttpResponseRedirect

from django.http import HttpResponse, response
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.conf import settings


#
#

# def fetch_pdf_resources(uri):
#     if uri.find(settings.MEDIA_URL) != -1:
#         path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
#     elif uri.find(settings.STATIC_URL) != -1:
#         path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
#     else:
#         path = None
#     return path


def render_to_pdf(tamplate_src, context_dict={}):
    tamplate = get_template(tamplate_src)
    html = tamplate.render(context_dict)
    result = BytesIO()

    # encode('UTF-8')), result,

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='utf-8', link_callback=fetch_pdf_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    'company': "ISOFT",
}


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('../templates/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('../templates/pdf.html', data)
        response = HttpResponse(pdf, content_type='appliocation/pdf')
        filename = 'Invoice_%s.pdf' % ("12341231")
        content = "attachment;filiename ='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


# from django.views import View
# from xhtml2pdf import pisa
#
#
# def render_to_pdf(template_src, context_dict):
#     result = BytesIO()
#     template = render_to_string(template_src, context_dict)
#     pdf = pisa.pisaDocument(BytesIO(template.encode('UTF-8')), result)
#
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#
#     return None


# app/views.py
from .utils import render_to_pdf


class GeneratePDF(View):
    def get(self, request):
        data = Sklad.objects.all()
        form = SkladForm()
        dataAC = Category.objects.all()
        dataishch = ishch.objects.all()
        if request.method == "POST":
            form = SkladForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('datatebles')
        context = {
            'data': data,
            'form': form,
            'datAC': dataAC,
            'dataishch': dataishch
        }
        # context = {
        #     'order_id': 1
        # }
        # template = 'pdf.html'
        pdf = render_to_pdf('../templates/kassa.html', context)

        if pdf:
            # filename = 'order_{}_{}.pdf'.format(int,1)
            # content = 'inline; filename="{}"'.format(filename)

            # if request.GET.get('save_to_file') == 'true':
            #     content = 'attachment; filename="{}"'.format(filename)

            response = HttpResponse(pdf, content_type=' application/pdf')
            # response['Content-Disposition'] = content
            return response

        return HttpResponse(status=404)
