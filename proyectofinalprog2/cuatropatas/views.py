from django.shortcuts import redirect, render
from django.http import HttpResponse

from cuatropatas.forms import RegisterOwner

# Create your views here.

def index (request):
    return render (request, "index.html")

def newUser (request):
    if request.method == 'POST':
        form = RegisterOwner(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index.html')
    else:
        form = RegisterOwner()
    return render (request, "newUser.html", {'form': form})

def official (request):
    return render (request, "Official.html")

def owner (request):
    return render (request, "Owner.html")

def vet (request):
    return render (request, "Vet.html")

