from django.db import models


class PedidoReposicao(models.Model):
    produto = models.IntegerField()
    quantidade = models.PositiveIntegerField()
    fornecedor = models.CharField(max_length=100)
    data_pedido = models.DateField(auto_now_add=True)
    status_choices = (
        ('Pendente', 'Pendente'),
        ('Processado', 'Processado'),
        ('Cancelado', 'Cancelado')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Pendente')

