from rest_framework import viewsets

from ..models.fornecedores import FornecedorModel
from ..serializers.fornecedores import FornecedorSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = FornecedorModel.objects.all()
    serializer_class = FornecedorSerializer
