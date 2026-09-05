from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            "f_name",
            "l_name",
            "email",
            "phone",
            "question",
            "message",
        ]

class LoginForm(forms.Form):

    username = forms.CharField( widget=forms.TextInput(attrs={"placeholder": "Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput( attrs={"placeholder": "••••••••"}))
    signin = forms.BooleanField(required=False)

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "••••••••"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "••••••••"}))