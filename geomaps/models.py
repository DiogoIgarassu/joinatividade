from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Alvo(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    data_expiracao = models.DateField()

    def __str__(self):
        return self.nome
