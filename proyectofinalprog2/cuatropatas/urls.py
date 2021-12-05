
from django.contrib import admin
from django.urls import path
from .views import editOwner, index, newUser, owner, vet, newVeterinary, logoutview, official, editVet, addPetCase

urlpatterns = [
    path('', index, name="index"),
    path('newUser/', newUser, name='newUser'),
    path('newVeterinary/', newVeterinary, name='newVeterinary'),
    path('Official/', official, name="official"),
    path('editOwner/', editOwner, name="editOwner"),
    path('Owner/', owner, name="owner"),
    path('Vet/', vet, name="vet"),
    path('addPetCase/', addPetCase, name="addPetCase"),
    path('editVet/', editVet, name="editVet"),
    path('logout/', logoutview, name="logout"),
    path('login/', index, name="login"),

]
