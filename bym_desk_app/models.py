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

class Ticket(models.Model):
    bloco = models.CharField(max_length=100, null=False)
    local = models.CharField(max_length=100, null=False)
    tipo = models.CharField(max_length=100, null=False)
    data = models.CharField(max_length=100, null=False)
    solicitante_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    analista_id = models.ForeignKey('Analista', on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

class Mensagem(models.Model):
    mensagem = models.CharField(max_length=255, null=False)
    imagem = models.CharField(max_length=100, null=False)
    ticket_id = models.ForeignKey('Ticket', on_delete=models.CASCADE)

    def __str__(self):
        return self.mensagem
