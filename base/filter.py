from .models import kassa
import django_filters


class KassaFilter(django_filters.FilterSet):
    class Meta:
        model = kassa
        fields = '__all__'
        exclude = ['date', 'comment', 'perechisleniya', 'qogpz', 'sum', 'bankhisob',]
