from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render
from webs.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')  

def shop(request):
    data=shopproduct.objects.all()
    return render(request,'shop.html',{'value':data})

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def account(request):
    return render(request,'myaccount.html',)

def register(request):
    return render(request,'signup.html')

def cart(request):
    obj = cartinfo.objects.all()

    return render(request,'cart.html',{'cart':obj})

def store(request):
    fn = request.GET.get('nm')
    ln = request.GET.get('lnm')
    em = request.GET.get('mail')
    ta = request.GET.get('value')

    # return HttpResponse(fn,ln,em,ta)
    obj=contactinfo(fname=fn,lname=ln,email=em,tarea=ta)
    obj.save()
    return render(request,'contact.html')


def data(request):
    name=request.POST['uname']
    mailid=request.POST['mail']
    password=request.POST['pwd']
    phone=request.POST['phone']
    address=request.POST['addres']

    obj1 = signupinfo(uname=name,umail=mailid,pswd=password,phn=phone,adrs=address)
    obj1.save()
    return render(request,'myaccount.html')

def linfo(request):
    loname=request.POST['eminm']
    lopwd=request.POST['lgpass']

    loname=str(loname)

    if loname is '':
        messages.warning(request,"name should not empty ......")
        return render(request,'myaccount.html')
        
    obj = signupinfo.objects.all()
    # obj1 = signupinfo.objects.all().filter(uname=loname) or signupinfo.objects.all().filter(umail=loname)

    for i in obj:
        if (i.uname==loname or i.umail==loname) and i.pswd==lopwd:
            # return render(request,'myaccount.html',{'store':obj1})
            messages.success(request,"login successfully .........")
            return render(request,'myaccount.html')
    
    # return HttpResponse("<h1>User not found</h1>")
    messages.error(request,"sorry user not found in database .......")
    return render(request,'myaccount.html')
        
def cartinfos(request):
    pid=request.POST['nm']
    pnam=request.POST['nm1']
    pprice=request.POST['nm2']
    pimage=request.POST['nm3']

    # obj=shopproduct.objects.all().filter(id=pid)
    obj1=cartinfo(pid=pid,pname=pnam,price=pprice,pimage=pimage)
    obj1.save()

    obj = cartinfo.objects.all()

    return render(request,'cart.html',{'cart':obj})

def delete(request):
    value=request.GET['value']
    obj=cartinfo.objects.all().filter(pid=value)
    obj.delete()

    output=cartinfo.objects.all()
    return render(request,'cart.html',{'cart':output})


def update(request):
    value=request.GET['id']
    pqty=request.GET['qty']
    pqty=int(pqty)
    pqty=pqty+1
    data = cartinfo.objects.get(pid=value)
    data.pquantity=pqty
    data.ptotalprice=int(data.ptotalprice)+50
    data.save()

    obj = cartinfo.objects.all()

    return render(request,'cart.html',{'cart':obj})


def uptodate(request):
    value=request.GET['id']
    pqty=request.GET['qty']
    pqty=int(pqty)
    pqty=pqty-1
    data = cartinfo.objects.get(pid=value)
    data.pquantity=pqty
    data.ptotalprice=int(data.ptotalprice)-50
    data.save()

    obj = cartinfo.objects.all()

    return render(request,'cart.html',{'cart':obj})


