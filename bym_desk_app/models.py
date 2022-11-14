from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome
