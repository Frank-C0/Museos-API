from django.contrib import admin
from .models import Autor, Sala, Exposicion, Museo
# Register your models here.

admin.site.register(Museo)
admin.site.register(Sala)
admin.site.register(Autor)
admin.site.register(Exposicion)