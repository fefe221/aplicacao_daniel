from django.db import models
from django.conf import settings

class Venda(models.Model):
    vendedor   = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='vendas',
        verbose_name='Vendedor'
    )
    descricao  = models.CharField(
        'Descrição', max_length=255
    )
    valor      = models.DecimalField(
        'Valor (R$)', max_digits=10, decimal_places=2
    )
    quantidade = models.PositiveIntegerField(
        'Quantidade', default=1
        )
    data       = models.DateTimeField(
        'Data da Venda', auto_now_add=True
    )

    class Meta:
        ordering = ['-data']
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return f'{self.descricao} — R$ {self.valor}'
