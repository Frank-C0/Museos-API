import django_filters
from .models import Autor, Sala, Exposicion, Museo

# filter for class: filter by contains
class MuseoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='contains')
    descripcion = django_filters.CharFilter(lookup_expr='contains')
    imagen = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Museo
        fields = ('nombre', 'descripcion', 'imagen')

class AutorFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='contains')
    apellido = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido')
class SalaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='contains')
    descripcion = django_filters.CharFilter(lookup_expr='contains')
    imagen = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Sala
        fields = ('nombre', 'descripcion', 'imagen')

# ExposicionFilter. also by autor and sala
class ExposicionFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='contains')
    tecnica = django_filters.CharFilter(lookup_expr='contains')
    categoria = django_filters.CharFilter(lookup_expr='contains')
    descripcion = django_filters.CharFilter(lookup_expr='contains')
    imagen = django_filters.CharFilter(lookup_expr='contains')
    autor_name = django_filters.CharFilter(field_name='autor__nombre', lookup_expr='contains')
    sala_name = django_filters.CharFilter(field_name='sala__nombre', lookup_expr='contains')
    class Meta:
        model = Exposicion
        fields = ('titulo', 'tecnica', 'categoria', 'descripcion', 'imagen', 'autor', 'sala', 'autor_name', 'sala_name')