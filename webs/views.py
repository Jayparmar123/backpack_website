from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from webs.models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

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
    # return render(request,'contact.html')
    return HttpResponseRedirect('/contact')


def data(request):
    name=request.POST['uname']
    mailid=request.POST['mail']
    password=request.POST['pwd']
    phone=request.POST['phone']
    address=request.POST['addres']

    obj1 = signupinfo(uname=name,umail=mailid,pswd=password,phn=phone,adrs=address)
    obj1.save()
    # return render(request,'myaccount.html')
    return HttpResponseRedirect('/account')

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

    # return render(request,'cart.html',{'cart':obj})
    return HttpResponseRedirect('/cart',{'cart':obj})

def delete(request):
    value=request.GET['value']
    obj=cartinfo.objects.all().filter(pid=value)
    obj.delete()

    output=cartinfo.objects.all()
    return render(request,'cart.html',{'cart':output})


def update(request):
    if request.method == 'POST':
        value = request.POST.get('id')
        pqty = request.POST.get('qty')
        pqty = int(pqty)

        data = cartinfo.objects.get(pid=value)
        data.pquantity = int(data.pquantity)
        data.pquantity += 1
        data.ptotalprice = int(data.ptotalprice)
        data.ptotalprice += 50
        data.save()
        if data.pquantity==0:
                data.delete()
        
        # Redirect to prevent data submission on page refresh
        return HttpResponseRedirect('/cart')  # Redirect to the same URL
    else:
        return redirect('index.html')


def uptodate(request):
    if request.method == 'POST':
        value = request.POST.get('id')
        pqty = request.POST.get('qty')
        pqty = int(pqty)

        data = cartinfo.objects.get(pid=value)
        data.pquantity = int(data.pquantity)
        data.pquantity -= 1
        data.ptotalprice = int(data.ptotalprice)
        data.ptotalprice -= 50
        data.save()
        if data.pquantity==0:
                data.delete()
        
        # Redirect to prevent data submission on page refresh
        return HttpResponseRedirect('/cart')  # Redirect to the same URL
    else:
        return redirect('index.html')

def forgotpass(request):
    if request.method == 'POST':
        user_name = request.POST.get('emnem')
        user_pass = request.POST.get('lgpass')
        user_p = request.POST.get('lgpa')
        obj = signupinfo.objects.all()
        if user_p == user_pass:
            for i in obj:
                if i.uname == user_name or i.umail == user_name:
                    i.pswd = user_p
                    i.save()
                    
                    # Redirect to account page after changing password
                    messages.success(request, "Password changed!.....")
                    return HttpResponseRedirect('/account')
            
            # If user not found
            messages.error(request, "Sorry, user not found...")
            return HttpResponseRedirect('/forgot')
        else:
            # If passwords don't match
            messages.error(request, "Sorry, passwords don't match...")
            return HttpResponseRedirect('/forgot')
    else:
        # If not a POST request
        return HttpResponseRedirect('/forgot')



def foorgoot(request):
    return render(request,'forgot.html')




