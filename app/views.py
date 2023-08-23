from django.shortcuts import render
from . models import *


def home(request):
 dels_of_the_day_products = Products.objects.all()
 cosmetics_obj = Categories.objects.get(name='Cosmetics')
 cosmetics = Products.objects.filter(categories=cosmetics_obj.id)
 categories = Categories.objects.all()
 context = {'dels_of_the_day_products':dels_of_the_day_products,'cosmetics':cosmetics,'categories':categories}
 return render(request, 'app/home.html',context)

# def base_file(request):
#  categories = Categories.objects.all()
#  context = {'categories':categories}
#  return render(request, 'app/base.html',context)

def product_detail(request,id):
 single_product = Products.objects.get(id=id)
 categories = Categories.objects.all()
 context={'categories':categories,'single_product':single_product}
 return render(request, 'app/productdetail.html',context)

def categories_page(request,id):
 products = Products.objects.filter(categories=id)
 categories = Categories.objects.all()
 display_categori = Categories.objects.get(id=id)
 context = {'categories':categories,'products':products,'display_categori':display_categori}
 return render(request, 'app/categories_page.html',context)

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
