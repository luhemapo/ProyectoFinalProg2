from django import forms
from django.forms import widgets
from .models import *

class RegisterOwner(forms.ModelForm):
    class Meta:
        model = Userapp

        fields = [
            'username',
            'email',
            'password',
            'role',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username *', 'required':True ,'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Your email *', 'required':True ,'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password *', 'required':True ,'class':'form-control'}),
            'role': forms.TextInput(attrs={'placeholder':'Name *', 'required':False ,'class':'form-control', 'value':'owner'}),
        }

