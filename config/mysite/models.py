from django.db import models

# Create your models here.

class Quadro(models.Model):
    Nome = models.CharField(max_length=50,blank=True, default="")
    Autor = models.CharField(max_length=50,blank=True, default="")
    Quadro = models.CharField(max_length=50,blank=True, default="")
    data_quadro = models.DateField(blank=True, default="")
    Quadrofoto = models.FileField(blank=True, default="")
    avaliacao = models.FloatField(default=0.0)
    descricao = models.CharField(max_length=1000000,blank=True, default="")
    def __str__(self):
        return self.Nome


class Tarefa(models.Model):
    Nome = models.CharField(max_length=100)
    descricao = models.TextField()
    feita = models.BooleanField(default=False)

    def __str__(self):
        return self.nome