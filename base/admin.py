from django.contrib import admin
from .models import Mijoz, Sklad, Category, ishch, sotibol, kassa, sharnoma, Tranzaksiya, sotilgan

admin.site.register(sotilgan)


# Register your models here.
class adminMijoz(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'eskiqarz', 'phone']
    list_filter = ['id', 'name', 'date', 'eskiqarz']
    search_fields = ['id', 'name', 'date', 'eskiqarz', 'phone']


class adminSklad(admin.ModelAdmin):
    list_display = ['id', 'name', 'num', 'price1', 'price2', 'data', 'new_date', 'status']
    list_filter = ['id', 'name', 'num', 'price1', 'price2', 'data', 'new_date', 'status']
    search_fields = ['id', 'name', 'num', 'price1', 'price2', 'data', 'new_date', 'status']


class adminCatagoriy(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'status']
    list_filter = ['id', 'name', 'date', 'status']
    search_fields = ['id', 'name', 'num', 'price1', 'price2', 'data', 'new_date', 'status']


class adminsotibol(admin.ModelAdmin):
    list_display = ['id', 'parent_id', 'prices', 'soni', 'date']
    list_filter = ['parent_id', 'prices', 'soni', 'date']
    search_fields = ['id', 'parent_id', 'prices', 'soni', 'date']


class adminishch(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'date', 'status']
    list_filter = ['name', 'phone', 'date', 'status']
    search_fields = ['name', 'phone', 'date']


class adminTranzaksiya(admin.ModelAdmin):
    list_display = ['id', 'name', 'summa', 'date']


admin.site.register(Mijoz, adminMijoz)
admin.site.register(Sklad, adminSklad)
admin.site.register(Category, adminCatagoriy)
admin.site.register(sotibol, adminsotibol)
admin.site.register(ishch, adminishch)
admin.site.register(kassa)
admin.site.register(Tranzaksiya,adminTranzaksiya)
admin.site.register(sharnoma)
