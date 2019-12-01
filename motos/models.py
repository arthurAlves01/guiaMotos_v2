from django.db import models

class Favoritos(models.Model):
    '''
    Classe que representa um registro na tabela de favoritos
    '''
    id_usuario = models.IntegerField(db_column="id_usuario", default=0)
    montadora = models.CharField(db_column="montadora", max_length=50, blank=True)
    modelo = models.CharField(db_column="modelo", max_length=50, blank=True)
    ano_modelo = models.CharField(db_column="ano_modelo", max_length=50, blank=True)
