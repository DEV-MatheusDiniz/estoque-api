from django.contrib import admin

from .models.vendas import VendasModel
from .models.venda_servicos import VendasServicoModel


admin.site.register(VendasModel)
admin.site.register(VendasServicoModel)
