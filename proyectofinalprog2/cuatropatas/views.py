from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView
from datetime import date
from django.urls import reverse_lazy

from cuatropatas.forms import RegisterOwner, RegisterUserO, RegisterVet, RegisterUserV, login, RegisterPet, addVisit,addPetCaseForm
from cuatropatas.models import Vet, Owner, Pet, Userapp, PetCase, Visit

# Create your views here.

def index (request):
    #if request.user.role == 'vet':
     #   return redirect('vet')

    if request.method == "POST":
        form = login(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                log(request, user)
                if user.role == 'vet':
                    return redirect ("vet")
                if user.role == 'owner':
                    return redirect ("owner")
                if user.role == 'official':
                    return redirect ("official")
    else:
        form=login()
    return render (request, "index.html", {'form':form})

def newUser (request):
    if request.method == 'POST':
        form_user = RegisterUserO(request.POST)
        form_owner = RegisterOwner(request.POST)
        if form_user.is_valid() and form_owner.is_valid():
            user= form_user.save()
            user.set_password(user.password)
            user.save()
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
            user.set_password(user.password)
            user.save()
            vet = form_vet.save()
            vet.userapp = user
            vet.save()
            return redirect('index')
    else:
        form_user = RegisterUserV()
        form_vet = RegisterVet()
    return render (request, "newVeterinary.html", {'form_user': form_user,'form_vet':form_vet })

def addPetCase(request):
    if request.method == "POST":
        form = addPetCaseForm(request.POST)
        if form.is_valid():
            created_at = date.today()
            petid= form.cleaned_data['pets']
            description= form.cleaned_data['description']
            type= form.cleaned_data['type']
            pet = Pet.objects.get(id=petid)
            new_case = PetCase(created_at=created_at, type=type, description=description, pet=pet)
            new_case.save()
            return redirect('owner')
    else:
        form= addPetCaseForm()
    return render (request, "addPetCase.html", {'form':form})

@login_required
def owner (request):
    user = request.user
    owner = Owner.objects.get(userapp_id = user.id)
    pet = owner.pet_set.all()
    visit = Visit.objects.all()
    petcase = PetCase.objects.all()
    if request.method == 'POST':
        form = RegisterPet(request.POST, request.FILES)
        print("*********************************")
        print(form.is_valid())
        print(form)
        if form.is_valid():
            birth = form.cleaned_data['birth']
            microchip = form.cleaned_data['microchip']
            name = form.cleaned_data['name']
            species = form.cleaned_data['species']
            race = form.cleaned_data['race']
            size = form.cleaned_data['size']
            sex = form.cleaned_data['sex']
            dangerous = form.cleaned_data['dangerous']
            sterilized = form.cleaned_data['sterilized']
            myowner = owner
            print(birth, microchip, name, species, race, size, sex, dangerous, sterilized, myowner)

            new_pet = Pet (microchip=microchip, name=name, species=species, race=race, size=size, sex=sex, birth=birth, dangerous=dangerous, sterilized=sterilized, owner=myowner)
            print("++++++++++++++++++++++++++++++++")
            print(new_pet)
            new_pet.save()
            return render (request, "Owner.html", {'form': form, 'pets':pet })
    else:
        form = RegisterPet()
    return render (request, "Owner.html", {'form': form, 'pets':pet,'visits':visit,'petcases':petcase })

@login_required
def vet (request):
    visit = Visit.objects.all()
    user = request.user
    if request.method == 'POST':
        form = addVisit(request.POST)
        print("---------------------------------")
        print(form.is_valid())
        if form.is_valid():
            created_at = date.today()
            petid= form.cleaned_data['pets']
            description= form.cleaned_data['description']
            type= form.cleaned_data['type']
            microchip= form.cleaned_data['microchip']
            pet = Pet.objects.get(id=petid)
            vet = Vet.objects.get(id=user.vet.id)
            new_visit = Visit(created_at=created_at, type=type, description=description,vet= vet, pet=pet)
            new_visit.save()
            if type == 'Microchip':
                pet.microchip = microchip
                pet.save()
            return redirect('vet')
    else:
        form = addVisit()
    return render (request, "Vet.html",{'form':form, 'visits':visit})

def logoutview (request):
    logout(request)
    return redirect ('index')


def official(request):
    owner = Owner.objects.all()
    pet = Pet.objects.all()
    petcase = PetCase.objects.all()
    visit = Visit.objects.all()
    contexto = {'owners':owner, 'pets':pet, 'petcases':petcase, 'visits': visit}
    return render(request, 'Official.html', contexto)

def editOwner (request):
    return render(request, 'editOwner.html')

def editVet (request):
    user = request.user
    if request.method == "POST":
        form=editVet(request.POST)
        if form.is_valid():
            print("Es valido")
    else:
        contexto = {
            'neighborhood':user.vet.neighborhood,
            'address': user.vet.address,
        }
        form = editVet(initial = contexto)
    print (user)
    return render(request, 'editVet.html',{'form':form})

    
    




