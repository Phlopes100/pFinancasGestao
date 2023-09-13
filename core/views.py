from rest_framework import viewsets
from .models import Tipo, Categoria, Controle
from .serializers import TipoSerializer, CategoriaSerializer, ControleSerializer


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ControleViewSet(viewsets.ModelViewSet):
    queryset = Controle.objects.all()
    serializer_class = ControleSerializer


