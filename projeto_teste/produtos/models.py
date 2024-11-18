from django.db import models

class produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.DecimalField(max_digits=8, decimal_places=2)
    descricao_produto = models.TextField()