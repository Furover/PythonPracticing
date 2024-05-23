from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    marca = models.TextField(max_length=255,default=0)
    valor = models.FloatField(default=0)
    estoque = models.IntegerField(default=0)