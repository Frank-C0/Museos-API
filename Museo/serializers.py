from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Autor, Sala, Exposicion, Museo
from .filters import AutorFilter, SalaFilter, ExposicionFilter, MuseoFilter


class ExposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposicion
        fields = '__all__'


class MuseoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Museo
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    # add a field a array of all exposiciones in the sala only for read
    exposiciones = ExposicionSerializer(many=True, read_only=True)

    class Meta:
        model = Sala
        fields = ['id', 'museo', 'nombre', 'descripcion', 'imagen', 'posX', 'posY', 'width', 'height', 'exposiciones', 'bg_color', 'border_color', 'border']




class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = '__all__' 


