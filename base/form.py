from django import forms
from .models import Mijoz, Sklad, Category, ishch, sotibol, kassa, sotilgan, Tranzaksiya, sharnoma


class MijozForm(forms.ModelForm):
    class Meta:
        model = Mijoz
        fields = "__all__"


class kassaForm(forms.ModelForm):
    class Meta:
        model = kassa
        fields = "__all__"


class sotibolForm(forms.ModelForm):
    class Meta:
        model = sotibol
        fields = "__all__"


class SkladForm(forms.ModelForm):
    class Meta:
        model = Sklad
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ishchiForm(forms.ModelForm):
    class Meta:
        model = ishch
        fields = '__all__'


class sotilganForm(forms.ModelForm):
    class Meta:
        model = sotilgan
        fields = '__all__'


class TranzaksiyaForm(forms.ModelForm):
    class Meta:
        model = Tranzaksiya
        fields = '__all__'
