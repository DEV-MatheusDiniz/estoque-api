from django.urls import path

from .views.vendas import VendasAPIView

urlpatterns = [
    path('vendas/', VendasAPIView.as_view()),
    path('vendas/<int:id>', VendasAPIView.as_view()),
]
