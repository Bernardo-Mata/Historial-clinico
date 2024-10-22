from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_historial_clinico, name='crear_historial_clinico'),
    path('', views.ver_historiales_clinicos, name= "ver_historiales_clinicos"),
    path('login/', views.login_usuario, name="login_usuario"),
    path('logout/', views.logout_usuario, name="logout_usuario"),
    path('registro/', views.registro_usuario, name='registro_usuario'),

]
