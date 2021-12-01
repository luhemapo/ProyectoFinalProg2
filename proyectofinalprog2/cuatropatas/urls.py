
from django.contrib import admin
from django.urls import path
from .views import index, newUser, official, owner, vet

urlpatterns = [
    path('', index),
    path('newUser/', newUser),
    path('Official/', official),
    path('Owner/', owner),
    path('Vet/', vet),

]
