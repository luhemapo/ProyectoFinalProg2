from collections import UserDict
from django import forms
from django.core.exceptions import ValidationError
from django.db.models.fields import TextField
from django.forms import widgets
from django.forms.fields import CharField
from .models import *
from django.utils.translation import ugettext_lazy as _

class login(forms.Form):
    username = CharField(widget=forms.TextInput( attrs={'placeholder':'Username *', 'required':True ,'class':'form-control'}))
    password = CharField(widget=forms.PasswordInput( attrs={'placeholder':'Password *', 'required':True ,'class':'form-control'}))
    
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
    
class RegisterPet(forms.Form):
    
    CHOICESspecies= [('Choose','Choose'),('Dog','Dog'),('Cat','Cat'),]
    species= forms.ChoiceField( choices = CHOICESspecies, widget=forms.Select(attrs= { 'default' : 1,'required' : True,'class' : 'form-select form-control',}))
    
    CHOICESsize= [('Choose','Choose'),('Small','Small'),('Medium','Medium'),('Big','Big'),]
    size= forms.ChoiceField( choices = CHOICESsize, widget=forms.Select(attrs= { 'default' : 1,'required' : True,'class' : 'form-select form-control',}))
    
    CHOICESsex= [('Choose','Choose'),('Male','Male'),('Female','Female'),]
    sex= forms.ChoiceField( choices = CHOICESsex, widget=forms.Select(attrs= { 'default' : 1,'required' : True,'class' : 'form-select form-control',}))
    
    CHOICESdang= [('Choose','Choose'),('Yes','Yes'),('No','No'),]
    dangerous= forms.ChoiceField( choices = CHOICESdang, widget=forms.Select(attrs= { 'default' : 1,'required' : True,'class' : 'form-select form-control',}))
    
    CHOICESsteril= [('Choose','Choose'),('Yes','Yes'),('No','No'),]
    sterilized= forms.ChoiceField( choices = CHOICESsteril, widget=forms.Select(attrs= { 'default' : 1,'required' : True,'class' : 'form-select form-control',}))
    
    birth= forms.DateField(required = True, widget=forms.DateInput(attrs= {'placeholder':'1998-12-25 *', 'class' : 'form-control'}))

    microchip = forms.CharField(required=True, widget=forms.NumberInput(attrs={'required':True ,'class':'form-control'}))

    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'required':True ,'class':'form-control'}))

    race = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'required':True ,'class':'form-control'}))
        
class editOwner(forms.Form):
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Your address *', 'required':True ,'class':'form-control'}))
    neighborhood = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Neighborhood *', 'required':True ,'class':'form-control'})) 
