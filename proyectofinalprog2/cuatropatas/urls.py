
from django.contrib import admin
from django.urls import path
from .views import editOwner, index, newUser, newPet, vet, newVeterinary, logoutview, owner_list, editVet

urlpatterns = [
    path('', index, name="index"),
    path('newUser/', newUser, name='newUser'),
    path('newVeterinary/', newVeterinary, name='newVeterinary'),
    path('Official/', owner_list, name="official"),
    path('editOwner/', editOwner, name="editOwner"),
    path('Owner/', newPet, name="owner"),
    path('Vet/', vet, name="vet"),
    path('editVet/', editVet, name="editVet"),
    path('logout/', logoutview, name="logout"),
    path('login/', index, name="login"),
    #(?P<id_pet>\d+)/$

]
