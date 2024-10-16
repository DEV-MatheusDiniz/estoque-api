from django.db import models

from api.clientes.models.clientes import ClienteModel


class VendasModel(models.Model):
    dt_venda = models.DateTimeField()
    nu_valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    fk_cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.dt_venda} - {self.nu_valor_total}"

    class Meta:
        app_label = "vendas"
        db_table = "vendas"
