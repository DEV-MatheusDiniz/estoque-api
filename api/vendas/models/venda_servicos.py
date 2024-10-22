from django.db import models

from .vendas import VendasModel
from api.servicos.models.servicos import ServicoModel


class VendaServicoModel(models.Model):
    nu_quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    nu_valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    fk_venda = models.ForeignKey(VendasModel, on_delete=models.CASCADE)
    fk_servico = models.ForeignKey(ServicoModel, on_delete=models.CASCADE)
    
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.fk_servico.ds_nome
    
    @property
    def nu_subtotal(self):
        return self.nu_quantidade * self.nu_valor_unitario

    class Meta:
        app_label = "vendas"
        db_table = "venda_servicos"
