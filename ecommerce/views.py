
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Category

def home(request):
    
    return render(request, "ecommerce/index.html")

def about(request):
    return render(request,"ecommerce/about.html")

def contact(request):
   return render(request,"ecommerce/contact.html")

def collection(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,"ecommerce/collection.html",{"products":products,"categories":categories})


