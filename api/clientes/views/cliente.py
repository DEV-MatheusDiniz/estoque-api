from rest_framework import viewsets

from ..models.clientes import ClienteModel
from ..serializers.clientes import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
