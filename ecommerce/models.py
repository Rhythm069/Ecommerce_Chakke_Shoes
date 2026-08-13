from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name= models.CharField(max_length=100)
    slug= models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
            return self.name

class Product(models.Model):
    name= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    stock=models.BooleanField(default=True)
    image=models.ImageField(upload_to="products/",blank=True,null=True)
    size=models.CharField(max_length=100,blank=True,null=True)
    material=models.CharField(max_length=100,blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    
class Customer(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to="profiles/",blank=True,null=True)
    phone_number=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)

class Hero(models.Model):
    image= models.ImageField(upload_to="hero/",blank=True,null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return "Hero Banner"

class Contact(models.Model):

    QUESTION_CHOICES = [
        ("general", "General question"),
        ("sizing", "Sizing help"),
        ("resole", "Resole service"),
        ("order", "Order status"),
        ("press", "Press & wholesale"),
    ]

    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)

    question = models.CharField(
        max_length=100,
        choices=QUESTION_CHOICES
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Cart(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="cart")
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    count = models.IntegerField(default=1, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
            return self.name