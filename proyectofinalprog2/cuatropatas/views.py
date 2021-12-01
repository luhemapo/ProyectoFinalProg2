from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, "index.html")

def newUser (request):
    return render (request, "newUser.html")

def official (request):
    return render (request, "Official.html")

def owner (request):
    return render (request, "Owner.html")

def vet (request):
    return render (request, "Vet.html")

