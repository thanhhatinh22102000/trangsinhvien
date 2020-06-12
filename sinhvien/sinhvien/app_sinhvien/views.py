from django.shortcuts import render,HttpResponse
from .models import thongtin,ketqua_ht,lichhoc
from .filters import thongtinfilters
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

class Loginclass(View):
    def get(self,request):
        return render(request,'app_sinhvien/login.html')

    def post(self,request):
        username=request.POST.get('taikhoan')
        password=request.POST.get('matkhau')
        myuser=authenticate(username=username,password=password)
        if myuser is None:
            return HttpResponse('<center><h1>User không tồn tại</h1></center>')
        else:
            login(request,myuser)
            return render(request,'app_sinhvien/hello.html')

class sinhvien_list(ListView):
    model = thongtin

class sinhvien_view(DetailView):
    model = thongtin

class sinhvien_create(CreateView):
    model = thongtin
    fields = ['hoten','msv','lop','quequan',]
    success_url = reverse_lazy('thongtin')

class sinhvien_update(UpdateView):
    model = thongtin
    fields = ['hoten','msv','lop','quequan',]
    success_url = reverse_lazy('thongtin')

class sinhvien_delete(DeleteView):
    model = thongtin
    success_url = reverse_lazy('thongtin')

class lichhoc_create(CreateView):
    model = lichhoc
    fields = ['hoten','tenmonhoc','tghoc','phonghoc',]
    success_url = reverse_lazy('lichhoc')

class lichhoc_update(UpdateView):
    model = lichhoc
    fields = ['hoten','tenmonhoc','tghoc','phonghoc',]
    success_url = reverse_lazy('lichhoc')

class lichhoc_delete(DeleteView):
    model = lichhoc
    success_url = reverse_lazy('lichhoc')

class ketqua_create(CreateView):
    model = ketqua_ht
    fields = ['hoten','tenmonhoc','sotinchhi','diem',]
    success_url = reverse_lazy('ketqua')

class ketqua_update(UpdateView):
    model = ketqua_ht
    fields = ['hoten','tenmonhoc','sotinchhi','diem',]
    success_url = reverse_lazy('ketqua')

class ketqua_delete(DeleteView):
    model = ketqua_ht
    success_url = reverse_lazy('ketqua')


class hello(View):
    def get(self,request):
        return render(request,'app_sinhvien/hello.html')

def thongtin_list(request):
    query=thongtin.objects.all()
    info_filter=thongtinfilters(request.GET,queryset=query)
    context={
        'form':info_filter.form,
        'info':info_filter.qs,
    }
    return render(request,'app_sinhvien/thongtin.html',context)

def ketqua_list(request):
    query=ketqua_ht.objects.all()
    kq_filter=thongtinfilters(request.GET,queryset=query)
    context={
        'form':kq_filter.form,
        'kq':kq_filter.qs,
    }

    return render(request,'app_sinhvien/ketqua.html',context)

def lichhoc_list(request):
    query=lichhoc.objects.all()
    lich_filter=thongtinfilters(request.GET,queryset=query)
    context={
        'form':lich_filter.form,
        'lich':lich_filter.qs,
    }

    return render(request,'app_sinhvien/lichhoc.html',context)