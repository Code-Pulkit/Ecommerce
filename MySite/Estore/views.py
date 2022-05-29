import imp
import re
from unicodedata import category
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from .models import Customer , Product , Cart , OrderPlaced
from .forms import CustomerRegistrationForm

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

def mobile(request , data=None):
    if data == None : 
        mobiles = Product.objects.filter(category = 'M')  
    elif data == 'Apple' or data == 'Samsung':
        mobiles = Product.objects.filter(category = 'M').filter(brand = data)
    elif data == 'below':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__lt= 10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__gte= 10000)
    return render(request, 'Estore/mobile.html' , {'mobiles' : mobiles})

# def customerregistration(request):
#  return render(request, 'Estore/customerregistration.html')

class CustomerResigrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'Estore/customerregistration.html' , {'form' : form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully.')
            form.save()
        return render(request, 'Estore/customerregistration.html', {'form':form})

def checkout(request):
 return render(request, 'Estore/checkout.html')
