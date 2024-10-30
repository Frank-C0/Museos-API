from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, SalaViewSet, ExposicionViewSet, MuseoViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'salas', SalaViewSet)
router.register(r'exposiciones', ExposicionViewSet)
router.register(r'museos', MuseoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
