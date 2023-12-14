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



class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Empregado(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class PerfilEmpregado(models.Model):
    empregado = models.OneToOneField(Empregado, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.empregado


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(Empregado)

    def __str__(self):
        return self.nome
