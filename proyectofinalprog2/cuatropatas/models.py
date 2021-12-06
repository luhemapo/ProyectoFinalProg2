from typing import AbstractSet
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Userapp(AbstractUser):
    role = models.CharField (max_length=15)
    

class Official(models.Model):
    userapp = models.OneToOneField(Userapp, null=True, blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

class Owner(models.Model):
    userapp = models.OneToOneField(Userapp, null=True, blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60, blank=True)
    neighborhood = models.CharField(max_length=30, blank=True)
    

class Vet(models.Model):
    userapp = models.OneToOneField(Userapp, null=True, blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60, null=False)
    neighborhood = models.CharField(max_length=30, null=False)

class Pet(models.Model):
    microchip = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=30)
    species = models.CharField (max_length=30)
    race = models.CharField (max_length=30)
    size = models.CharField (max_length=30)
    sex = models.CharField (max_length=15)
    picture = models.ImageField (upload_to="img", null=True)
    birth = models.DateField()
    dangerous= models.CharField(max_length=5)
    sterilized= models.CharField(max_length=5)
    owner = models.ForeignKey(Owner, null=False, on_delete=models.CASCADE)

class PetCase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField (max_length=15)
    description = models.CharField (max_length=240)
    pet = models.ForeignKey(Pet, null=False, on_delete=models.CASCADE)

class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField (max_length=15)
    description = models.CharField (max_length=240)
    pet = models.ForeignKey(Pet, null=False, on_delete=models.CASCADE)
    vet = models.ForeignKey(Vet, null=False, on_delete=models.CASCADE)


