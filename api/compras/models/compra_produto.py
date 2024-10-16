from django.db import models

from .compras import ComprasModel
from api.produtos.models.produtos import ProdutoModel


class CompraProdutoModel(models.Model):
    fk_compra = models.ForeignKey(ComprasModel, on_delete=models.CASCADE)
    fk_produto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE)
    nu_quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    nu_valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    nu_subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.fk_produto

    class Meta:
        app_label = "compras"
        db_table = "compra_produto"
