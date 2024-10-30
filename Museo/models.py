from django.db import models
from colorfield.fields import ColorField

class Museo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.URLField(blank=True, null=True)
    width = models.FloatField()
    height = models.FloatField()
    bg_color = ColorField(default="#04ff00")
    border_color = ColorField(default="#0000ff")
    border = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Sala(models.Model):
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.URLField(blank=True, null=True)
    posX = models.FloatField()
    posY = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    bg_color = ColorField(default="#04ff00")
    border_color = ColorField(default="#0000ff")
    border = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class Exposicion(models.Model):
    sala = models.ForeignKey(Sala, related_name='exposiciones', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True, null=True)
    tecnica = models.CharField(max_length=100) 
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    ano = models.IntegerField()
    imagen = models.URLField(blank=True, null=True)
    posX = models.FloatField(default=0)
    posY = models.FloatField(default=0)
    width = models.FloatField(default=0.2)
    height = models.FloatField(default=0.2)
    bg_color = ColorField(default="#04ff00")
    border_color = ColorField(default="#0000ff")
    border = models.BooleanField(default=True)
    absolute_position = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo