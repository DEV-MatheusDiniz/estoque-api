from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from api.clientes.views.cliente import ClienteViewSet
from api.fornecedores.views.fornecedores import FornecedorViewSet
from api.servicos.views.servicos import ServicoViewSet
from api.produtos.views.produtos import ProdutoViewSet


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('fornecedores', FornecedorViewSet)
router.register('servicos', ServicoViewSet)
router.register('produtos', ProdutoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('', include('api.vendas.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
