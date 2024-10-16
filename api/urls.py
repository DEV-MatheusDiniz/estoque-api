from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.clientes.views.cliente import ClienteViewSet
from api.fornecedores.views.fornecedores import FornecedorViewSet
from api.servicos.views.servicos import ServicoViewSet


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('fornecedores', FornecedorViewSet)
router.register('servicos', ServicoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
