from django.db import models
from django.contrib.auth.models import User

from api.clientes.models.clientes import ClienteModel


class VendasModel(models.Model):
    dt_venda = models.DateTimeField(null=True, blank=True)
    nu_valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bo_finalizado = models.BooleanField(default=False)
    
    fk_cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    fk_funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.dt_venda} - {self.nu_valor_total}"

    class Meta:
        app_label = "vendas"
        db_table = "vendas"
