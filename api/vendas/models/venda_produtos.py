from django.db import models

from .vendas import VendasModel
from api.produtos.models.produtos import ProdutoModel


class VendaProdutoModel(models.Model):
    nu_quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    nu_valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    nu_subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    fk_venda = models.ForeignKey(VendasModel, on_delete=models.CASCADE)
    fk_produto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE)
    
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.fk_produto.ds_nome

    class Meta:
        app_label = "vendas"
        db_table = "venda_produtos"
