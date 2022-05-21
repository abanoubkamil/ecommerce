
from django.shortcuts import render,redirect
from .models import category,product,cart
# Create your views here.

def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory,'item':cart.objects.all().count()})

def Category(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    allproducts = product.objects.all().filter(category_id = categoryid )
    return render(request,'pages/category.html',{"allproducts":allproducts,"allcategory":allcategory,"mycategory":mycategory,'item':cart.objects.all().count()})


def Product(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid)
    return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct,'item':cart.objects.all().count()})

def newproducts(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    return render(request,'pages/newproducts.html',{"allproducts":allproducts,"allcategory":allcategory,'item':cart.objects.all().count()})

def cart1(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    return render(request,'pages/cart.html',{"allproducts":allproducts,"allcategory":allcategory,"cars":cart.objects.all()})

def add(request,proid):
    a=int(cart.objects.filter(pid=proid).count())
    if a >= 1:
        s=cart.objects.get(pid=proid)
        cart.objects.filter(pid=proid).update(num=int(s.num)+1)
    else:
        carts=cart(pid=proid,num=1)
        carts.save()
    return redirect("/")

def delet(request,proid):
    a=int(cart.objects.filter(pid=proid).count())
    if a!=0:
        q=cart.objects.get(pid=proid)
        if q.num >1:
            cart.objects.filter(pid=proid).update(num=int(q.num)-1)
        
        else:
            q.delete()
    return redirect("/cart/")
