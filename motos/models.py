from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BuscaFavorita(models.Model):
    usuario = models.ManyToOneRel(User, related_name="favorito")
    montadora = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    ano =  models.CharField(max_length=4, null=False)