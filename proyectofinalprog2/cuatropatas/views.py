from django.shortcuts import redirect, render
from django.http import HttpResponse

from cuatropatas.forms import RegisterOwner, RegisterUserO, RegisterVet, RegisterUserV

# Create your views here.

def index (request):
    return render (request, "index.html")

def newUser (request):
    if request.method == 'POST':
        form_user = RegisterUserO(request.POST)
        form_owner = RegisterOwner(request.POST)
        if form_user.is_valid() and form_owner.is_valid():
            user= form_user.save()
            owner = form_owner.save()
            owner.userapp = user
            owner.save()
            return redirect('index')
    else:
        form_user = RegisterUserO()
        form_owner = RegisterOwner()
    return render (request, "newUser.html", {'form_user': form_user,'form_owner': form_owner })

def newVeterinary (request):
    if request.method == 'POST':
        form_user = RegisterUserV(request.POST)
        form_vet = RegisterVet(request.POST)
        if form_user.is_valid() and form_vet.is_valid():
            user= form_user.save()
            vet = form_vet.save()
            vet.userapp = user
            vet.save()
            return redirect('index')
    else:
        form_user = RegisterUserV()
        form_vet = RegisterVet()
    return render (request, "newVeterinary.html", {'form_user': form_user,'form_vet':form_vet })
    

def official (request):
    return render (request, "Official.html")

def owner (request):
    return render (request, "Owner.html")

def vet (request):
    return render (request, "Vet.html")

