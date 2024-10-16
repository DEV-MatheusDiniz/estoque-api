from django.contrib import admin

from .models.produtos import ProdutoModel
from .models.categorias import ProdutoCategoriaModel
from .models.tipos import ProdutoTipoModel


admin.site.register(ProdutoModel)
admin.site.register(ProdutoCategoriaModel)
admin.site.register(ProdutoTipoModel)
