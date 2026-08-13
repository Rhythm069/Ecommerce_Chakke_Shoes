
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product,Category,Hero
from .forms import ContactForm

def home(request):
     hero = Hero.objects.filter(active=True).first()
     return render(request, "ecommerce/index.html",{"hero":hero})

def about(request):
    return render(request,"ecommerce/about.html")

def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            print("Contact saved:", contact)

            return redirect("ecommerce:contact")

        else:
            print("Error form:", form.errors)

    else:
        form = ContactForm()

    return render(
        request,
        "ecommerce/contact.html",
        {
            "form": form
        })                                 

def collection(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,"ecommerce/collection.html",{"products":products,"categories":categories})

def login(request):
    return render (request,"ecommerce/login.html")


