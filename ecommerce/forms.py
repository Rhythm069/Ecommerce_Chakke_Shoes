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

