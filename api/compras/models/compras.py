from django.db import models

from api.fornecedores.models.fornecedores import FornecedorModel


class ComprasModel(models.Model):
    dt_compra = models.DateTimeField()
    fk_fornecedor = models.ForeignKey(FornecedorModel, on_delete=models.CASCADE)
    nu_valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.dt_compra} - {self.nu_valor_total}"

    class Meta:
        app_label = "compras"
        db_table = "compras"
