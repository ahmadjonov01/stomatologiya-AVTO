"""djangoProject5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from . import views1
from . import pdfdowload

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('ViewPDF/', pdfdowload.ViewPDF.as_view(), name='login'),
    path('', views.index, name='index'),
    path('filter/', views.KassaFilter, name='kassafilter'),
    # path('pdf_view/', views1.fetch_pdf_resources, name='pdf_view'),
    # path('pdf_view/', views1.GeneratePDF.as_view(), name='pdf_view'),
    path('pdf_view/', views1.ViewPDF.as_view(), name='pdf_view'),
    # path('download_pdf/', views1.DownloadPDF.as_view(), name='download_pdf'),
    path('datatables/', views.datatebles, name='datatebles'),
    path('make_active/<int:pk><str:str>', views.make_active, name='make_active'),
    path('delets/<int:pk><str:str>', views.deletes, name='deletes'),
    path('out_of_defult/<int:pk><str:str>', views.out_of_defult, name='out_of_defult'),
    path('dataTablesCategory/', views.dataTablesCategory, name='dataTablesCategory'),
    path('datateblesMijoz/', views.datateblesMijoz, name='datateblesMijoz'),
    path('dataTablesishch/', views.dataTablesishch, name='dataTablesishch'),
    path('dataTableskassa/', views.dataTableskassa, name='dataTableskassa'),
    path('datateblesSotilgan/', views.datateblesSotilgan, name='datateblesSotilgan'),
    path('datateblesTranzaksiya/', views.datateblesTranzaksiya, name='datateblesTranzaksiya'),
    path('dataTablessotibol/', views.dataTablessotibol, name='dataTablessotibol'),
    path('formSklad/', views.formSklad, name='ormSklad'),
    path('editform/<int:pk>', views.editform, name='editform'),
    path('skladviwe/<int:pk>', views.sklad, name='sklad'),
    path('chart/', views.chart, name='chart'),
    path('inline/', views.chart1, name='inline'),
    path('sotilganmaxsulotlar/', views.sotilganmaxsulotlar, name='sotilganmaxsulotlar'),
    path('kassamaxsusjadval/', views.kassamaxsusjadval, name='kassamaxsusjadval'),
    path('kategoriya/<int:id>', views.kategoriya, name='kategoriya'),
    path('ishlabchiqaruvchilar/<int:id>', views.ishlabchiqaruvchilar, name='ishlabchiqaruvchilar'),
    path('Mijozlar/<int:id>', views.Mijozlar, name='Mijozlar'),
    path('Tranzaksiya/<int:id>', views.Tranzaksiyaviwe, name='Tranzaksiya'),
    path('protuct41/<int:id>', views.sotibolinga, name='protuct41'),
    path('export_pdf/<int:pk><str:shaxs>', views.export_pdf, name='export_pdf'),
    path('error/', views.error, name='error'),
    path('kategoriyaedit/<int:id>', views.kategoriyaedit, name='kategoriyaedit'),
    path('Mijozedit/<int:id>', views.Mijozedit, name='Mijozedit'),
    path('ishlabchiqaruvedit/<int:id>', views.ishlabchiqaruvedit, name='ishlabchiqaruvedit'),
    path('dataTablessotiboledit/<int:id>', views.dataTablessotiboledit, name='dataTablessotiboledit'),
    path('mijoz_chart/<int:id>', views.mijoz_chart, name='mijoz_chart'),
    path('mavjud_emas/<int:id>', views.mavjud_emas, name='mavjud_emas'),

]
handler404 = "base.views.page_not_found_view"
