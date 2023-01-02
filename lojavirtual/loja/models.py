from django.db import models
import uuid


class Roupa(models.Model):
    TAMANHO = (
        ('Pequeno', 'P'),
        ('Médio', 'M'),
        ('Grande', 'G'),
        ('Extra Grande', 'GG')
    )
    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, unique=True)
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    modelo = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=20, choices=TAMANHO, blank=False, null=False)
    quantidade = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
