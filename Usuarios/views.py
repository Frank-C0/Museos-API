from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from dj_rest_auth.views import LoginView

# Aplica @csrf_exempt al endpoint de login si usas un endpoint basado en clases
# @csrf_exempt
class CustomLoginView(LoginView):
    pass