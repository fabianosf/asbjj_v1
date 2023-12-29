from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=14, blank=True, null=True)
    mensagem = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    