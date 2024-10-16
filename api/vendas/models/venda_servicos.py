from django.db import models

from .vendas import VendasModel
from api.servicos.models.servicos import ServicoModel


class VendasServicoModel(models.Model):
    dt_venda = models.DateTimeField()
    nu_valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    fk_venda = models.ForeignKey(VendasModel, on_delete=models.CASCADE)
    fk_servico = models.ForeignKey(ServicoModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.dt_venda} - {self.nu_valor_total}"

    class Meta:
        app_label = "vendas"
        db_table = "venda_servicos"
