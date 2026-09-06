
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Product,Category,Hero
from django.contrib.auth.decorators import login_required
from .forms import ContactForm,LoginForm,RegisterForm   



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

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect("ecommerce:home")

        else:

            return render(
                request,
                "ecommerce/login.html",
                {
                    "Form": LoginForm(),
                    "error": "Invalid username or password."
                }
            )

    
    return render(request,"ecommerce/login.html",{ "Form": LoginForm()})



def registers(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("confirm_password")

            if password != confirm_password:
                form.add_error("confirm_password", "Passwords do not match.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
            
    return render(request,"ecommerce/registers.html",{"Form":RegisterForm()})

@login_required
def cart (request):
    return render(request, "ecommerce/cart.html")