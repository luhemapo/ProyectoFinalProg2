
from django.contrib import admin
from django.urls import path
from .views import index, newUser, official, owner, vet, newVeterinary

urlpatterns = [
    path('', index, name="index"),
    path('newUser/', newUser, name='newUser'),
    path('newVeterinary/', newVeterinary, name='newVeterinary'),
    path('Official/', official, name="official"),
    path('Owner/', owner, name="owner"),
    path('Vet/', vet, name="vet"),

]
