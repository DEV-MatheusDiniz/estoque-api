from rest_framework import viewsets

from ..models.produtos import ProdutoModel
from ..serializers.produtos import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = ProdutoModel.objects.all()
    serializer_class = ProdutoSerializer
