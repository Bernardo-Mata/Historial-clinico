"""
URL configuration for Historial_clinico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mi_aplicacion import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('historiales/', include('mi_aplicacion.urls')),
    path('historiales/crear/', views.crear_historial_clinico, name='crear_historial_clinico'),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('historiales/ver/', include('mi_aplicacion.urls'), name='ver_historial_clinico'),

]
