from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from .models import *

class RegisterUserO(forms.ModelForm):
    role=CharField(initial='owner', required=False, widget=forms.HiddenInput(attrs={'default':'owner', 'value':'owner'}) )
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
        }

class RegisterOwner(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            'name',
            'address',
            'neighborhood',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name *', 'required':True ,'class':'form-control'}),
            'address': forms.TextInput(attrs={'placeholder':'Your address *', 'required':True ,'class':'form-control'}),
            'neighborhood': forms.TextInput(attrs={'placeholder':'Neighborhood *', 'required':True ,'class':'form-control'}),   
        }

class RegisterUserV(forms.ModelForm):
    role=CharField(initial='vet', required=False, widget=forms.HiddenInput(attrs={'default':'vet', 'value':'vet'}) )
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
        }

class RegisterVet(forms.ModelForm):
    class Meta:
        model = Vet

        fields = [
            'name',
            'address',
            'neighborhood',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name *', 'required':True ,'class':'form-control'}),
            'address': forms.TextInput(attrs={'placeholder':'Your address *', 'required':True ,'class':'form-control'}),
            'neighborhood': forms.TextInput(attrs={'placeholder':'Neighborhood *', 'required':True ,'class':'form-control'}),   
        }
    

