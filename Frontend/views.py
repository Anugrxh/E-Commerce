import razorpay
from django.shortcuts import render, redirect
from AdminApp.models import catagorydb
from AdminApp.models import productdb
from Frontend.models import contactdb, signupdb, cartdb, bookingdb
from django.contrib import messages

# Create your views here.


def index_pagee(request):
    cat = catagorydb.objects.all()
    pro = productdb.objects.order_by('?')[:4]
    return render(request,"index_pagee.html",{'cat':cat , 'pro':pro})

def product_page(request):
    pro = productdb.objects.all()
    cat = catagorydb.objects.all()
    return render(request,"Products.html",{'pro':pro , 'cat':cat})

def catagory_pro(request,cat_name):
    data = productdb.objects.filter(catname=cat_name)
    return render(request,"Catagory_pro.html",{'data':data})

def single_product(request,pro_id):
    data = productdb.objects.get(id=pro_id)
    return render(request,"product_single.html",{'data':data})

def contact_us(request):
    return render(request,"contact_us.html")

def about_us(request):
    return render(request,"about_us.html")

def service(request):
    return render(request,"service.html")

def contactdata(request):
    if request.method == "POST":
        fulna = request.POST.get('fullname')
        conum = request.POST.get('contactnumber')
        ema = request.POST.get('email')
        sta = request.POST.get('state')
        cit = request.POST.get('city')
        sugg =request.POST.get('suggestion')
        obj = contactdb(fullname=fulna,contactnumber=conum,email=ema,state=sta,city=cit,suggestion=sugg)
        obj.save()
        return redirect(contact_us)


#USER SIGN IN AND LOGIN

def signup_user(request):
    return render(request,"signup_user.html")

def login_user(request):
    return render(request,"login_user.html")

def signupdata(request):
    if request.method == "POST":
        fulna = request.POST.get('fullname')
        mob = request.POST.get('mobile')
        ema  = request.POST.get('email')
        una = request.POST.get('username')
        pas = request.POST.get('password')
        obj = signupdb(fullname=fulna,mobile=mob,email=ema,username=una,password=pas)
        obj.save()
        return redirect(signup_user)

def Userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if signupdb.objects.filter(username=un,password=pwd).exists():
            request.session['username']= un
            request.session['password']= pwd
            messages.success(request,"Login success")
            return redirect(index_pagee)
        else:
            messages.error(request,"Invalid username or password..")
            return redirect(login_user)
    else:
        return redirect(login_user)

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_user)


#CART


def cart_page(request):
    data = cartdb.objects.filter(username=request.session['username'])
    total_price=0
    for i in data:
        total_price = total_price + i.totalprice
    return render(request,"Cart_page.html",{'data':data , 'total_price':total_price})

def cartdata(request):
    if request.method == "POST":
        una = request.POST.get('username')
        pna = request.POST.get('pname')
        qua = request.POST.get('quantity')

        tpri = request.POST.get('totalprice')
        des = request.POST.get('description')
        obj = cartdb(username=una,pname=pna,quantity=qua,totalprice=tpri,description=des)
        obj.save()
        messages.success(request,"Item added to cart")
        return redirect(cart_page)

def cart_delete(request,pro_id):
    pro = cartdb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request,"Item deleted from cart")
    return redirect(cart_page)

#checkout page

def checkout_page(request):
    data = cartdb.objects.filter(username=request.session['username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.totalprice
    return render(request,"Checkout.html",{'data':data , 'total_price':total_price})

#SEARCH PRODUCT PAGE

def product_search(request):
    pro = productdb.objects.all()
    cat = catagorydb.objects.all()
    return render(request,"product_search.html",{'pro':pro,'cat':cat})


def bookingdata(request):
    if request.method=="POST":
        usr = request.POST.get('username')
        fna = request.POST.get('fullname')
        ema = request.POST.get('email')
        addr = request.POST.get('address')
        cty = request.POST.get('city')
        bkdpro = request.POST.get('bookedproduct')
        pin = request.POST.get('pincode')
        mob = request.POST.get('mobile')
        ttpri = request.POST.get('totalprice')
        obj = bookingdb(username=usr,fullname=fna,email=ema,address=addr,city=cty,bookedproduct=bkdpro,pincode=pin,mobile=mob,totalprice=ttpri)
        obj.save()
        return redirect(payment_product)


def payment_product(request):

    last_object = bookingdb.objects.order_by('-id').first()
    payy = last_object.totalprice
    payy_str_hotel = str(payy)
    for ptotl in payy_str_hotel:
        print(ptotl)

    if request.method == "POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_jcVIUHkalKhqwa','Gwt5sgqFhjy0ur0qJUKQxTwY'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"Payment_page.html",{'payy_str_hotel':payy_str_hotel})