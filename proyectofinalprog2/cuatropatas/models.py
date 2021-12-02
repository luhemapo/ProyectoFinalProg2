from django.db import models

# Create your models here.

class Userapp(models.Model):
    username = models.CharField(primary_key = True, max_length=30, unique=True, null=False)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=30)
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
    picture = models.CharField (max_length=120)
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


