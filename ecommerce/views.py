
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    
    return render(request, "ecommerce/index.html")

def about(request):
    return render(request,"ecommerce/about.html")

def contact(request):
   return render(request,"ecommerce/contact.html")

def collection(request):
   return render(request,"ecommerce/collection.html",)


