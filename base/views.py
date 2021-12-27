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


# from django import db.models.query.QuerySet


@login_required(login_url='login_user')
def index(request):
    data2 = Sklad.objects.all().count()
    data = Mijoz.objects.all().count()
    datas = sotilgan.objects.all().count()

    date1 = datetime.now().strftime('%Y-%m-%d')
    sotilgan_dict = sotilgan.objects.filter(date=date1)
    # print(type(sotilgan_dict))
    g = None
    for i in sotilgan_dict:
        g = i
    print(g)
    import urllib.request
    import json

    # url = 'https://kun.uz/uz/news/list?f=recommended'

    if g != None:
        print('salom')

        class MyDict(dict):

            def __setitem__(self, key, value):
                if key in self:
                    super().__setitem__(key, self[key] + value)
                else:
                    super().__setitem__(key, value)

        #
        # print(date1)
        for i in sotilgan_dict:
            d = MyDict({i.product_id.name: 0, })
        for i in sotilgan_dict:
            d[i.product_id.name] = i.soni
    else:
        d = {'00': 00}
    print(d)
    context = {
        'data': data,
        'datas': datas,
        'data2': data2,
        'd': d,
        'date': date1,
    }
    return render(request, 'index.html', context)


def datateblesSotilgan(request):
    data = sotilgan.objects.all()
    dataTA = Tranzaksiya.objects.all()
    form = sotilganForm()
    dataAC = Sklad.objects.all()
    if request.method == "POST":
        form = sotilganForm(request.POST)
        if form.is_valid():
            form.save()
            d1 = form.data.get('date')
            print(d1)
            # da2 = form.data.get('product_id')
            # print(da2)
            da = Sklad.objects.get(id=form.data.get('product_id'))
            # print()
            da.soni = int(da.soni) - int(form.data.get('soni'))
            if int(da.soni) == da.num or int(da.soni) < da.num or da.soni == str(da.num):
                return redirect('error')
            elif int(da.soni) > da.num:
                da.save()
                return redirect('datateblesSotilgan')
    context = {
        'data': data,
        'form': form,
        'dataTA': dataTA,
        'dataAC': dataAC,

    }
    return render(request, 'data1.html', context)


def error(request):
    return render(request, 'error.html')


def datateblesTranzaksiya(request):
    data = Tranzaksiya.objects.all()
    form = TranzaksiyaForm()
    dateC = Mijoz.objects.all()
    if request.method == 'POST':
        form = TranzaksiyaForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('datateblesTranzaksiya')
    context = {
        'data': data,
        'form': form,
        'dataC': dateC,
    }
    return render(request, 'data2.html', context)


def datatebles(request):
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
    return render(request, 'data3.html', context)


def datateblesMijoz(request):
    data = Mijoz.objects.all()
    form = MijozForm()
    if request.method == 'POST':
        form = MijozForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('datateblesMijoz')

    context = {
        'data': data,
        'form': form,
        'datAC': sharnoma.objects.all()

    }
    return render(request, 'data4.html', context)


def dataTablesCategory(request):
    data = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'data': data,
        'form': form
    }
    return render(request, 'data5.html', context)


def dataTablesishch(request):
    data = ishch.objects.all()
    form = ishchiForm()
    if request.method == 'POST':
        form = ishchiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dataTablesishch')

    context = {
        'data': data,
        'form': form
    }
    return render(request, 'data6.html', context)


def dataTablessotibol(request):
    data = sotibol.objects.all()
    form = sotibolForm()
    datasklad = Sklad.objects.all()
    dataAC = Category.objects.all()
    if request.method == 'POST':
        form = sotibolForm(request.POST)
        print(form)

        if form.is_valid():
            form.is_valid()
            form.save()
            d1 = form.data.get('date')
            print(d1)
            da = Sklad.objects.get(id=form.data.get('parent_id'))
            da.soni = int(da.soni) + int(form.data.get('soni'))
            da.save()
            form.save()
        return redirect('dataTablessotibol')

    context = {

        'data': data,
        'form': form,
        'dataAC': dataAC,
        'dataISHCH': ishch.objects.all(),
        'datasklad': datasklad,
    }
    return render(request, 'data7.html', context)


def dataTablessotiboledit(request, id):
    data = sotibol.objects.filter(id=id)
    form = sotibolForm()
    datasklad = Sklad.objects.all()
    dataAC = Category.objects.all()
    if request.method == 'POST':
        form = sotibolForm(request.POST)
        print(form)

        if form.is_valid():
            form.is_valid()
            form.save()
            # d1 = form.data.get('date')
            data.soni = form.data.get('soni')
            data.parent_id = form.data.get('parent_id')
            data.ish_ch_id = form.data.get('ish_ch_id')
            data.prices = form.data.get('prices')

        return redirect('dataTablessotibol')

    context = {

        'data': data,
        'form': form,
        'dataAC': dataAC,
        'dataISHCH': ishch.objects.all(),
        'datasklad': datasklad,
    }
    return render(request, 'sotibolinganedit.html', context)


def dataTableskassa(request):
    data = kassa.objects.all()
    dataTA = Mijoz.objects.all()
    form = kassaForm()
    dataAC = Category.objects.all()
    my_filter = KassaFilter(request.GET, queryset=data)
    data = my_filter.qs
    if request.method == 'POST':
        form = kassaForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()

    context = {
        'data': data,
        'my_filter': my_filter.form,
        'form': form,
        'dataTA': dataTA,
        'dataAC': dataAC,
    }
    return render(request, 'data8.html', context)


def formSklad(request):
    form = SkladForm()
    if request.method == "POST":
        form = SkladForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'data': Category.objects.all()
    }
    return render(request, 'form.html', context)


def make_active(request, pk, str):
    if str == 'Sklad':
        data = Sklad.objects.get(id=pk)
        data.status = True
        data.save()
    if str == "Category":
        data = Category.objects.get(id=pk)
        data.status = True
        data.save()
    if str == 'Mijoz':
        data = Mijoz.objects.get(id=pk)
        data.status = True

        data.save()
    if str == "ishch":
        data = ishch.objects.get(id=pk)
        data.status = True
        data.save()
    if str == "sotibol":
        data = sotibol.objects.get(id=pk)
        data.status = True
        data.save()
    if str == "Tranzaksiya":
        data = Tranzaksiya.objects.get(id=pk)
        data.status = True
        data.save()
    if str == "sotilgan":
        data = sotilgan.objects.get(id=pk)
        data.status = True
        data.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def out_of_defult(request, pk, str):
    if str == 'Sklad':
        data = Sklad.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "Category":
        data = Category.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == 'Mijoz':
        data = Mijoz.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "ishch":
        data = ishch.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "sotibol":
        data = sotibol.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if str == "Tranzaksiya":
        data = Tranzaksiya.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "sotilgan":
        data = sotilgan.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deletes(request, pk, str):
    if str == 'Sklad':
        data = Sklad.objects.get(id=pk)
        data.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "Category":
        data = Category.objects.get(id=pk)
        data.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == 'Mijoz':
        data = Mijoz.objects.get(id=pk)
        data.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "ishch":
        data = ishch.objects.get(id=pk)
        data.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "sotibol":
        data = sotibol.objects.get(id=pk)
        data.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if str == "Tranzaksiya":
        data = Tranzaksiya.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if str == "sotilgan":
        data = sotilgan.objects.get(id=pk)
        data.status = False
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def editform(request, pk):
    data1 = Sklad.objects.filter(id=pk)
    form = SkladForm()
    da = Sklad.objects.get(id=pk)

    dataAC = Category.objects.all()
    if request.method == 'POST':
        form = SkladForm(request.POST)
        # print(form)
        da.name = form.data.get('name')
        da.unique_id = form.data.get('unique_id')
        # da.category = (form.data.get('category'))
        da.price1 = form.data.get('price1')
        da.num = form.data.get('num')
        da.soni = form.data.get('soni')
        daD = form.data.get('category')
        da.save()
        print(daD)
        return redirect('datatebles')
    context = {
        'data': data1,
        'form': form,
        'datAC': dataAC
    }
    return render(request, 'formedit.html', context)


def kategoriyaedit(request, id):
    data = Category.objects.filter(id=id)
    form = CategoryForm()
    date = Category.objects.get(id=id)
    # dataAC = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print(form)
        if form.is_valid():
            date.name = form.data.get('name')
            date.sort = form.data.get('sort')
            date.save()

            return redirect('index')
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'kategoriyaedit.html', context)


def Mijozedit(request, id):
    data = Mijoz.objects.filter(id=id)
    form = MijozForm()
    date = Mijoz.objects.get(id=id)
    if request.method == 'POST':
        form = MijozForm(request.POST)
        # print(form)
        if form.is_valid():
            date.name = form.data.get('name')
            date.phone = form.data.get('phone')
            date.address = form.data.get('address')
            date.bankname = form.data.get('bankname')
            date.inn = form.data.get('inn')
            date.pasport = form.data.get('pasport')
            date.oked = form.data.get('oked')
            date.mfo = form.data.get('mfo')
            date.kimtomon = form.data.get('kimtomon')
            date.hisob = form.data.get('hisob')
            date.eskiqarz = form.data.get('eskiqarz')
            date.date = form.data.get('date')
            # date. = form.data.get('date')
            date.save()
            return redirect('index')
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'mijozlaredit.html', context)


def sklad(request, pk):
    data = Sklad.objects.filter(id=pk)
    context = {
        'data': data
    }
    return render(request, 'sklad.html', context)


def chart(request):
    global sklad_dict
    datateblesSotilgan = sotilgan.objects.all()
    dataTranzaksiya = Tranzaksiya.objects.all()

    class MyDict(dict):

        def __setitem__(self, key, value):
            if key in self:
                super().__setitem__(key, self[key] + value)
            else:
                super().__setitem__(key, value)

    for i in sotilgan.objects.all():
        d = MyDict({i.product_id.name: 0, })
    for i in sotilgan.objects.all():
        d[i.product_id.name] = i.soni

    for i in Sklad.objects.all():
        sklad_dict = MyDict({i.name: 0, })
    for i in Sklad.objects.all():
        sklad_dict[i.name] = int(i.soni)
    print(sklad_dict)

    for i in sotilgan.objects.all():
        mijozlar_dict = MyDict({i.transaction_id.name.name: 0, })
    for i in sotilgan.objects.all():
        mijozlar_dict[i.transaction_id.name.name] = int(i.soni)
    soni = 0

    for fo in Tranzaksiya.objects.all():
        for foo1 in sotilgan.objects.all():
            if foo1.transaction_id.name == fo.name:
                print(foo1.product_id.name)
                dict1 = MyDict({foo1.product_id.name: 0})
                dict1[foo1.product_id.name] = foo1.soni
    print(d)
    context = {
        'datateblesSotilgan': datateblesSotilgan,
        'dataTranzaksiya': dataTranzaksiya,
        'sklad': sklad_dict,
        'd': d,
        'mijozlar_dict': mijozlar_dict,

    }

    return render(request, 'chartjs.html', context)


def chart1(request):
    return render(request, 'inline.html')


def sotilganmaxsulotlar(request):
    data = sotilgan.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'sotilganmaxsulotlar.html', context)


def kassamaxsusjadval(request):
    data = kassa.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'kassjadval.html', context)


def kategoriya(request, id):
    data = Category.objects.filter(id=id)
    context = {
        'data': data,
    }
    return render(request, 'kategoriya.html', context)


def ishlabchiqaruvchilar(request, id):
    data = ishch.objects.filter(id=id)
    context = {
        'data': data,
    }
    return render(request, 'kategoriya.html', context)


def Mijozlar(request, id):
    data = Mijoz.objects.filter(id=id)
    context = {
        'data': data,
    }
    return render(request, 'mijoz.html', context)


def Tranzaksiyaviwe(request, id):
    data = Tranzaksiya.objects.filter(id=id)
    context = {
        'data': data,
    }
    return render(request, 'Tranzaksiyajadvali.html', context)


def sotibolinga(request, id):
    data = sotibol.objects.filter(id=id)
    context = {
        'data': data,
    }
    return render(request, 'sotilganmaxsulotlar.html', context)


def ishlabchiqaruvedit(request, id):
    data = ishch.objects.filter(id=id)
    form = ishchiForm()
    date = ishch.objects.get(id=id)
    if request.method == 'POST':
        form = ishchiForm(request.POST)
        if form.is_valid():
            date.name = form.data.get('name')
            date.phone = form.data.get('phone')
            date.email = form.data.get('email')
            date.sahifa = form.data.get('sahifa')
            date.save()
            return redirect('index')
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'ishlabchiqaruvedit.html', context)


def page_not_found_view(request, exception):
    return render(request, 'pages/examples/404.html', status=404)


def mijoz_chart(request, id):
    class MyDict(dict):
        def __setitem__(self, key, value):
            if key in self:
                super().__setitem__(key, self[key] + value)
            else:
                super().__setitem__(key, value)

    data = None

    for di in sotilgan.objects.all():
        for q in sotilgan.objects.filter(transaction_id=di.transaction_id):
            data = q
        if data != None:
            if di.transaction_id.id == id:
                for i in sotilgan.objects.filter(transaction_id=di.transaction_id):
                    data = MyDict({i.product_id.name: 0, })
                for i in sotilgan.objects.filter(transaction_id=di.transaction_id):
                    data[i.product_id.name] = i.soni

                for d in sotilgan.objects.filter(transaction_id=di.transaction_id):
                    t = MyDict({d.transaction_id.name.name: 0, })
                for d in sotilgan.objects.filter(transaction_id=di.transaction_id):
                    t[d.transaction_id.name.name] = 1
        # if t == None:
        #     return redirect('index')

    context = {
        'data': data,
        'name': t,
    }

    return render(request, 'mijozlarchartjs.html', context)


def mavjud_emas(request, id):
    tran = Mijoz.objects.filter(id=id)
    context = {
        'tran': tran,
    }
    return render(request, 'mavjudemas.html', context)


from django.http import HttpResponse
from reportlab.pdfgen import canvas


def export_pdf(request, pk, shaxs):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="shartnoma.pdf"'
    for i in Tranzaksiya.objects.filter(id=pk):
        p = (i.id)
    p = canvas.Canvas(response)
    p.drawString(10, 780, shaxs)
    p.drawString(10, 775, p)
    p.showPage()
    p.save()
    return response

#
# def product_list(request):
#     f = KassaFilter(request.GET, queryset=kassa.objects.all())
#     dataTA = Mijoz.objects.all()
#     form = kassaForm()
#     dataAC = Category.objects.all()
#
#     if request.method == 'POST':
#         form = kassaForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         # 'data': data,
#         'form': form,
#         'dataTA': dataTA,
#         'dataAC': dataAC,
#         'filter': f,
#     }
#     return render(request, 'kassa.html', context)
