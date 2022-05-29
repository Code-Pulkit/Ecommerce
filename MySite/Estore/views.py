import re
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer , Product , Cart , OrderPlaced

# def home(request):
#  return render(request, 'Estore/home.html')
class ProductView(View) : 
    def get(self , request) : 
        mobiles =  Product.objects.filter(category = 'M')
        topwears = Product.objects.filter(category = 'TW')
        bottomwears = Product.objects.filter(category = 'BW')
        return render(request , 'Estore/home.html' , {'mobiles' : mobiles})

# def product_detail(request):
#  return render(request, 'Estore/productdetail.html')
class ProductDetailView(View):
    def get(self,request, pk):
        product = Product.objects.get(pk=pk)
        return render(request , 'Estore/productdetail.html' , {'product' : product})

def add_to_cart(request):
 return render(request, 'Estore/addtocart.html')

def buy_now(request):
 return render(request, 'Estore/buynow.html')

def profile(request):
 return render(request, 'Estore/profile.html')

def address(request):
 return render(request, 'Estore/address.html')

def orders(request):
 return render(request, 'Estore/orders.html')

def change_password(request):
 return render(request, 'Estore/changepassword.html')

def mobile(request):
 return render(request, 'Estore/mobile.html')

def login(request):
 return render(request, 'Estore/login.html')

def customerregistration(request):
 return render(request, 'Estore/customerregistration.html')

def checkout(request):
 return render(request, 'Estore/checkout.html')
