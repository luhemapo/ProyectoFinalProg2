from django.shortcuts import redirect, render
from django.http import HttpResponse

from cuatropatas.forms import RegisterOwner, RegisterUser, RegisterVet

# Create your views here.

def index (request):
    return render (request, "index.html")

def newUser (request):
    if request.method == 'POST':
        form_user = RegisterUser(request.POST)
        form_owner = RegisterOwner(request.POST)
        form_vet = RegisterVet(request.POST)
        if form_user.is_valid() and form_owner.is_valid():
            user= form_user.save()
            owner = form_owner.save()
            owner.userapp = user
            owner.save()
            return redirect('index')
        if form_user.is_valid() and form_vet.is_valid():
            user= form_user.save()
            vet = form_vet.save()
            vet.userapp = user
            vet.save()
            return redirect('index')
    else:
        form_user = RegisterUser()
        form_owner = RegisterOwner()
        form_vet = RegisterVet()
    return render (request, "newUser.html", {'form_user': form_user,'form_owner': form_owner, 'form_vet':form_vet })

def newVeterinary (request):
    return render (request, "newVeterinary.html")

def official (request):
    return render (request, "Official.html")

def owner (request):
    return render (request, "Owner.html")

def vet (request):
    return render (request, "Vet.html")

