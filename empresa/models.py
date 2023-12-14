from django.db import models


class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    nome_cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_cargo


class Pessoas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    admissao = models.DateField()

    def __str__(self):
        return self.nome
