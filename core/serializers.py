from rest_framework import serializers
from .models import Tipo, Categoria, Controle


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controle
        fields = '__all__'