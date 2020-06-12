from django.urls import path
from .views import thongtin_list,ketqua_list,lichhoc_list,hello,sinhvien_create,sinhvien_delete,sinhvien_update,lichhoc_create,lichhoc_update,lichhoc_delete,ketqua_create,ketqua_update,ketqua_delete,Loginclass

urlpatterns = [
    path('hello/',hello.as_view(),name='hello'),
    path('',Loginclass.as_view(),name='login'),
    path('info/',thongtin_list,name='thongtin'),
    path('lichhoc/',lichhoc_list,name='lichhoc'),
    path('ketqua/',ketqua_list,name='ketqua'),

    path('create_info/',sinhvien_create.as_view(),name='create'),
    path('update_info/<int:pk>',sinhvien_update.as_view(),name='update'),
    path('delete_info/<int:pk>',sinhvien_delete.as_view(),name='delete'),

    path('create_lich/',lichhoc_create.as_view(),name='create_lich'),
    path('update_lich/<int:pk>',lichhoc_update.as_view(),name='update_lich'),
    path('delete_lich/<int:pk>',lichhoc_delete.as_view(),name='delete_lich'),

    path('create_kq/',ketqua_create.as_view(),name='create_kq'),
    path('update_kq/<int:pk>',ketqua_update.as_view(),name='update_kq'),
    path('delete_kq/<int:pk>',ketqua_delete.as_view(),name='delete_kq'),
]