from django.db import models

class Roupa(models.Model):
    TAMANHO = (
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande"),
        ("GG", "Extra Grande")
    )
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    modelo = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=2, choices=TAMANHO, blank=False, null=False)
    
    def __str__(self):
        return self.nome
