from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import HistorialClinicoForm
from .models import HistorialClinico, Paciente, Doctor
from .forms import PacienteForm, RegistroUsuarioForm
from django.views.decorators.http import require_POST


# Create your views here.

def inicio(request):
    return render(request, "index.html")

def crear_historial_clinico(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        historial_form = HistorialClinicoForm(request.POST)
        if paciente_form.is_valid() and historial_form.is_valid():
            paciente = paciente_form.save()
            historial_clinico = historial_form.save(commit=False)
            historial_clinico.paciente = paciente
            historial_clinico.usuario = request.user
            
            historial_clinico.save()
            return redirect('ver_historiales_clinicos')
    else:
        paciente_form = PacienteForm()
        historial_form = HistorialClinicoForm()
    return render(request, 'crear_historial_clinico.html', {
        'paciente_form': paciente_form,
        'historial_form': historial_form
    })


def ver_historiales_clinicos(request):
    historiales = HistorialClinico.objects.filter(usuario=request.user)
    pacientes = Paciente.objects.all()
    return render(request, 'ver_historiales_clinicos.html', {'historiales': historiales, 'pacientes': pacientes})

#login y logout
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ver_historiales_clinicos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


#@require_POST
def logout_usuario(request):

    logout(request)
    return redirect('inicio')

# registro de usuarios
def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('ver_historiales_clinicos')
    else:
            form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})
