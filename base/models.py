from django.db import models


# Create your models here.
class sharnoma(models.Model):
    class Meta:
        verbose_name = 'Shart noma'

    name = models.CharField(verbose_name='sharnoma nomi', max_length=2131232)
    data = models.FileField(upload_to='static/shartnomalar')

    def __str__(self):
        return str(self.id) + ')' + self.name


class Mijoz(models.Model):
    class Meta:
        verbose_name = 'Kilent'

    name = models.CharField(blank=True, max_length=2000, verbose_name='F.I.O')
    phone = models.CharField(max_length=13, verbose_name='Telefon nomer')
    eskiqarz = models.FloatField(blank=True, max_length=20000, verbose_name='Eski qarz')
    pasport = models.CharField(blank=True, max_length=20200, verbose_name='Pasport s/r')
    kimtomon = models.CharField(blank=True, max_length=20000, verbose_name='Kim tomonidan berilgan')
    date = models.DateField(verbose_name='Amal qillish muddati')
    inn = models.IntegerField(verbose_name='INN')
    bankname = models.CharField(blank=True, max_length=20000, verbose_name='Bank nomi')
    hisob = models.CharField(blank=True, max_length=2000, verbose_name='Hisob raqam')
    mfo = models.CharField(blank=True, max_length=2000, verbose_name="MFO")
    oked = models.CharField(blank=True, max_length=2000, verbose_name="OKED")
    created_at = models.DateField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    address = models.CharField(blank=True, max_length=999999999, verbose_name='Manzili')


class Tranzaksiya(models.Model):
    name = models.ForeignKey('Mijoz', models.CASCADE, blank=True, null=True)
    summa = models.CharField(max_length=2000, verbose_name='Summa')
    date = models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana')

    def __str__(self):
        return self.name


class Sklad(models.Model):
    class Meta:
        verbose_name = 'Sklad (Ombor)'

    unique_id = models.CharField(max_length=2000, verbose_name='Unique ID')
    name = models.CharField(max_length=2000, verbose_name='Nomi')
    manufacturer = models.ForeignKey('ishch', models.CASCADE)
    category = models.ForeignKey('Category', models.CASCADE)
    soni = models.IntegerField(verbose_name='Soni(donada)')
    price1 = models.FloatField(max_length=2000, verbose_name='Kelgan narxi')
    price2 = models.FloatField(max_length=2000, verbose_name='Sotish narxi')
    num = models.IntegerField(verbose_name='..dan kam qolganda ogohlantirish')
    data = models.DateField(auto_now_add=True, verbose_name='Yaratilgan Sana')
    new_date = models.DateField(auto_now=True, verbose_name='Yangilanga Sana', null=False)
    status = models.BooleanField(max_length=2000, verbose_name='Holati')

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Katagoriya'

    name = models.CharField(max_length=2000, verbose_name="Kategoriya nomi")
    sort = models.IntegerField()
    date = models.DateField(auto_now_add=True, verbose_name='Yaratilgan Sana')
    status = models.BooleanField(auto_created=True, verbose_name='Holati')

    def __str__(self):
        return self.name


class ishch(models.Model):
    class Meta:
        verbose_name = 'Ishlab chiqaruvchi (tovarlar shu odamdan olinadi)'

    name = models.CharField(max_length=2000, verbose_name='Ishlab chiqaruvchi Nomi')
    phone = models.CharField(max_length=13, verbose_name='Telefon nomer uz')
    date = models.DateField(auto_now_add=True, verbose_name='Yaratlgan sana')
    status = models.BooleanField(max_length=20, verbose_name='Holati')
    email = models.EmailField(verbose_name='Email')
    sahifa = models.CharField(max_length=20000000)

    def __str__(self):
        return self.name


class sotibol(models.Model):
    class Meta:
        verbose_name = 'Sotib olingan produktlar'

    ish_ch_id = models.ForeignKey('ishch', models.CASCADE, blank=True, null=True,
                                  verbose_name='Ishlab chiqarivchi ID')
    parent_id = models.ForeignKey('Sklad', models.CASCADE, verbose_name='Product ID')
    soni = models.IntegerField(verbose_name='Maxsulot soni')
    prices = models.FloatField(max_length=200, verbose_name='Ummumiy narxi')
    date = models.DateField(auto_now_add=True, verbose_name='Yaratilgan sana', null=False)


class kassa(models.Model):
    class Meta:
        verbose_name = "KASSA"

    kilent_id = models.ForeignKey('Mijoz', models.CASCADE, verbose_name='Mijoz ID')
    sum = models.FloatField(max_length=2000, verbose_name='SO`M(UZS-so`m)')
    qogpz = models.FloatField(max_length=2000, verbose_name='Qog`oz(USD-$)')
    bankhisob = models.CharField(max_length=20000, verbose_name='Bank hisobi')
    perechisleniya = models.CharField(max_length=20000, verbose_name='Perechisleniya')
    date = models.DateField(auto_now_add=True, verbose_name='Sanasi')
    comment = models.CharField(max_length=2000000000000, verbose_name='Comment')


class sotilgan(models.Model):
    class Meta:
        verbose_name = 'Sotilgan Maxsulot'

    transaction_id = models.ForeignKey('Tranzaksiya', models.CASCADE, blank=True, null=True,
                                       verbose_name='Transaction ID')
    product_id = models.ForeignKey('Sklad', models.CASCADE, verbose_name="Product ID")
    soni = models.IntegerField(verbose_name='Soni')
    price = models.FloatField(max_length=20000, verbose_name='Narxi')
    skidka = models.CharField(max_length=20000, verbose_name='Skidka')
    skidkali_narxi = models.FloatField(max_length=20000, verbose_name='Skidkali narxi')
    date = models.DateField(verbose_name='Yaratilgan sana', auto_now_add=True)
