from django.db import models

# Create your models here.

class contactinfo(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    tarea=models.TextField()

    def __str__(self):
        return self.fname
    
class signupinfo(models.Model):
    uname=models.CharField(max_length=20)
    umail=models.CharField(max_length=30)
    pswd=models.CharField(max_length=30)
    phn=models.IntegerField()
    adrs=models.TextField()

    def __str__(self):
        return self.uname
    
class shopproduct(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    pimage=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.pname

class cartinfo(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    pquantity=models.CharField(max_length=2,default=1)
    ptotalprice=models.CharField(max_length=10,default=50)
    pimage=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.pname
    
class getinfos(models.Model):
    pluss=models.IntegerField()
    minuss=models.IntegerField()