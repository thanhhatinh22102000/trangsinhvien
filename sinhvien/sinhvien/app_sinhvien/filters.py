from django import forms
import django_filters
from .models import thongtin,lichhoc,ketqua_ht
from django_filters import DateFilter

class thongtinfilters(django_filters.FilterSet):
    class Meta:
        model=thongtin
        fields=('hoten',)

class lichhocfilters(django_filters.FilterSet):
    class Meta:
        model=lichhoc
        fields=('hoten',)

class ketquafilters(django_filters.FilterSet):
    class Meta:
        model=ketqua_ht
        fields=('hoten',)