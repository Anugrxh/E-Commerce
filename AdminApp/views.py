from django.shortcuts import render, redirect

from AdminApp.models import catagorydb, productdb

from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from Frontend.models import contactdb, bookingdb
from django.contrib import messages

# Create your views here.


    #catagory



def indexx(request):
    messages.success(request, "login success..!")
    return render(request,"indexx.html")

def add_cat(request):
    return render(request,"AddCat.html")

def catdata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = catagorydb(name=na,description=des,image=img)
        obj.save()
        messages.success(request,"Catagory Added..")
        return redirect(add_cat)

def display_cat(request):
    data = catagorydb.objects.all()
    return render(request,"DisplayCat.html",{'data':data})

def edit_catagory(request,dataid):
    cat = catagorydb.objects.get(id=dataid)

    return render(request,"EditCat.html",{'cat':cat})

def update_catagory(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catagorydb.objects.get(id=dataid).image
        catagorydb.objects.filter(id=dataid).update(name=na,description=des,image=file)
        messages.success(request,"Edited Successfully")
        return redirect(display_cat)

def delete_catagory(request,dataid):
    data = catagorydb.objects.filter(id=dataid)
    data.delete()
    messages.error(request,"Deleted Successfully...!")
    return redirect(display_cat)






    #Product






def add_product(request):
    cat = catagorydb.objects.all()
    return render(request,"ProductAdd.html",{'cat':cat})

def productdata(request):
    if request.method == "POST":
        cna = request.POST.get('catname')
        pna = request.POST.get('productname')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        img = request.FILES['image']
        obj = productdb(catname=cna,productname=pna,description=des,price=pri,image=img)
        obj.save()
        messages.success(request,"Product Added..")

        return redirect(add_product)

def product_display(request):
    data = productdb.objects.all()
    return render(request,"ProductDisplay.html",{'data':data})



def Product_edit(request,pro_id):
    cat = catagorydb.objects.all()
    product = productdb.objects.get(id=pro_id)
    return render(request, "ProductEdit.html", {'cat':cat , 'product': product})

def product_update(request,pro_id):
    if request.method == "POST":
        cna = request.POST.get('catname')
        pna = request.POST.get('productname')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=pro_id).image
        productdb.objects.filter(id=pro_id).update(catname=cna,productname=pna,description=des,price=pri,image=file)
        messages.success(request,"Edited Successfully")

        return redirect(product_display)

def product_delete(request,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.error(request,"Product Deleted")
    return redirect(product_display)




 #ADMIN





def admin_login(request):


    return render(request,"Admin_login.html")



def adminlogin(request):
    if request.method=="POST":
        una = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=una).exists():
            x = authenticate(username=una,password=pwd)

            if x is not None:
                login(request,x)
                request.session['username'] = una
                request.session['password'] = pwd

                return redirect(indexx)


            else:
                messages.error(request,"Error")

                return redirect(admin_login)

        else:

            return redirect(admin_login)



def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)


#CUSTOMER SUGGESTION

def contact_suggestion(request):
    data = contactdb.objects.all()
    return render(request,"contact_suggestion.html",{'data':data})

def delete_contact_suggestion(request,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(contact_suggestion)


def bookingsss(request):
    data = bookingdb.objects.all()
    return render(request,"Bookingss.html",{'data':data})
