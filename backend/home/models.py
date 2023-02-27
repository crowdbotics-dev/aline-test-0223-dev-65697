from django.conf import settings
from django.db import models
class Breed(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,blank=True,)
class Pet(models.Model):
    'Generated Model'
    name = models.CharField(max_length=200,)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    birth_date = models.DateField()
    breed = models.ForeignKey("home.Breed",on_delete=models.SET_NULL,null=True,blank=True,related_name="pet_breed",)
