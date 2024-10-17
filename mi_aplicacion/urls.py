from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_historial_clinico, name='crear_historial_clinico'),
    path('', views.ver_historiales_clinicos, name= "ver_historiales_clinicos")
]
