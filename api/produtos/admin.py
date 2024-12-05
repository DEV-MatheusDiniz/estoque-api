from django.contrib import admin

from .models.produtos import ProdutoModel
from .models.categorias import ProdutoCategoriaModel


admin.site.register(ProdutoModel)
admin.site.register(ProdutoCategoriaModel)
