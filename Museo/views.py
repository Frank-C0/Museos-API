from rest_framework import viewsets
from .models import Autor, Sala, Exposicion, Museo
from .serializers import AutorSerializer, SalaSerializer, ExposicionSerializer, MuseoSerializer
from .filters import AutorFilter, SalaFilter, ExposicionFilter, MuseoFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MuseoViewSet(viewsets.ModelViewSet):
    queryset = Museo.objects.all()
    serializer_class = MuseoSerializer

    # set filter backend
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # set filter fields
    filterset_class = MuseoFilter
    # set ordering fields
    ordering_fields = ('nombre', 'descripcion', 'imagen')
    # set search fields
    search_fields = ('nombre', 'descripcion', 'imagen')
    # set ordering
    ordering = ('nombre',)

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    # set filter backend
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # set filter fields
    filterset_class = SalaFilter
    # set ordering fields
    ordering_fields = ('nombre', 'descripcion', 'imagen')
    # set search fields
    search_fields = ('nombre', 'descripcion', 'imagen')
    # set ordering
    ordering = ('nombre',)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    # set filter backend
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # set filter fields
    filterset_class = AutorFilter
    # set ordering fields
    ordering_fields = ('nombre', 'apellido')
    # set search fields
    search_fields = ('nombre', 'apellido')
    # set ordering
    ordering = ('nombre',)


class ExposicionPagination(PageNumberPagination):
    page_size = 6 
    page_size_query_param = 'page_size'  
    max_page_size = 10  

class ExposicionViewSet(viewsets.ModelViewSet):
    queryset = Exposicion.objects.all()
    serializer_class = ExposicionSerializer
    pagination_class = ExposicionPagination  # Añade la paginación aquí

    # set filter backend
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # set filter fields
    filterset_class = ExposicionFilter
    # set ordering fields
    ordering_fields = ('titulo', 'tecnica', 'categoria', 'descripcion', 'imagen', 'autor', 'sala')
    # set search fields
    search_fields = ('titulo', 'tecnica', 'categoria', 'descripcion', 'imagen', 'autor', 'sala')
    # set ordering
    ordering = ('titulo',)


