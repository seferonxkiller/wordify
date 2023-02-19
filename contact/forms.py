from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Name"
        })
        self.fields['phone'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Phone"
        })
        self.fields['email'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Email"
        })
        self.fields['message'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Write Message"
        })
