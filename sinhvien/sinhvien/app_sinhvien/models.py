from django.db import models


class thongtin(models.Model):
    hoten=models.CharField(max_length=100,null=False,blank=False)
    msv=models.CharField(max_length=30,null=False,blank=False)
    lop=models.CharField(max_length=10)
    quequan=models.CharField(max_length=30)

    def __str__(self):
        return self.hoten


class ketqua_ht(models.Model):
    hoten=models.CharField(max_length=100,null=False,blank=False)
    tenmonhoc=models.CharField(max_length=100,null=False,blank=False)
    sotinchhi=models.IntegerField()
    diem=models.IntegerField()

    def __str__(self):
        return self.tenmonhoc

class lichhoc(models.Model):
    hoten=models.CharField(max_length=100,null=False,blank=False)
    tenmonhoc=models.CharField(max_length=100,null=False,blank=False)
    tghoc=models.CharField(max_length=100)
    phonghoc=models.CharField(max_length=10)

    def __str__(self):
        return self.tenmonhoc

    class Meta:
        default_related_name='app_sinhvien'