from rest_framework import viewsets

from ..models.servicos import ServicoModel
from ..serializers.servicos import ServicoSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = ServicoModel.objects.all()
    serializer_class = ServicoSerializer
