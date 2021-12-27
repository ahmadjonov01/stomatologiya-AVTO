# from io import BytesIO
# from tempfile import template
#
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.views import View
# from xhtml2pdf import pisa
#
#
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
#
#
# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):
#         if request.method == "POST":
#             date_from = request.POST.get("date_from")
#         date_to = request.POST.get("date_to")
#         select = request.POST.get("select")
#         # a = db_cart.objects.all().filter(updated_at__lte=date_to, updated_at__gte=date_from, stage=select, status=1)
#         pdf = render_to_pdf('../templates/pdf.html')
#         return HttpResponse(pdf, content_type='application/pdf')
#
#
# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('../templates/pdf.html')
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "report%s.pdf" % ("12341231")
#         content = "attachment; filename='%s'" % (filename)
#         response['Content-Disposition'] = content
#         return response
#
#
# class ViewPDF(View):
#
#     def get(self, request, *args, **kwargs):
#         context = {}  # Add something to your context object here
#         pdf = render_to_pdf('pdf.html', context)
#         return pdf
