
from django.contrib import admin
from django.urls import path
from .views import index, newUser, newPet, vet, newVeterinary, logoutview, owner_list

urlpatterns = [
    path('', index, name="index"),
    path('newUser/', newUser, name='newUser'),
    path('newVeterinary/', newVeterinary, name='newVeterinary'),
    path('Official/', owner_list, name="official"),
    path('Owner/', newPet, name="owner"),
    path('Vet/', vet, name="vet"),
    path('logout/', logoutview, name="logout"),
    path('login/', index, name="login"),

]
