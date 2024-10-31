from django.urls import path

from .views.vendas import VendasAPIView
from .views.venda_servicos import VendaServicosAPIView

urlpatterns = [
    path('vendas/', VendasAPIView.as_view()),
    path('vendas/<int:id>', VendasAPIView.as_view()),
    
    path('vendas/servicos/', VendaServicosAPIView.as_view()),
    path('vendas/<int:id_venda>/servicos/', VendaServicosAPIView.as_view()),
    path('vendas/<int:id_venda>/servicos/<int:id_venda_servico>/', VendaServicosAPIView.as_view()),
]
