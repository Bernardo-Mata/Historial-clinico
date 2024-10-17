from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HistorialClinicoForm
from .models import HistorialClinico, Paciente
from .forms import PacienteForm

# Create your views here.


def crear_historial_clinico(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        historial_form = HistorialClinicoForm(request.POST)
        if paciente_form.is_valid() and historial_form.is_valid():
            paciente = paciente_form.save()
            historial_clinico = historial_form.save(commit=False)
            historial_clinico.paciente = paciente
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
    historiales = HistorialClinico.objects.all()
    pacientes = Paciente.objects.all()
    return render(request, 'ver_historiales_clinicos.html', {'historiales': historiales, 'pacientes': pacientes})
