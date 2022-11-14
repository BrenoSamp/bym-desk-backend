from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    senha = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome

class Analista(models.Model):
    setor = models.CharField(max_length=100, null=False)
    matricula = models.CharField(max_length=100, null=False, unique=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.matricula
