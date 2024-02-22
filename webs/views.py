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
    return render(request,'cart.html')

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
        
def cartinfo(request):
    pid=request.POST['nm']

    obj=shopproduct.objects.all().filter(id=pid)

    return render(request,'cart.html',{'shop':obj})