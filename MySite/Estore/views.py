from django.shortcuts import render

def home(request):
 return render(request, 'Estore/home.html')

def product_detail(request):
 return render(request, 'Estore/productdetail.html')

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
