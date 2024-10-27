from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# class Usuario( models.Model):
#     ROLES = (
#         ('doctor', 'Doctor'),
#         ('paciente', 'Paciente'),
#     )
#     rol = models.CharField(max_length=10, choices=ROLES, default='doctor'),
#     nombre = models.CharField(max_length=100)
#     apellidos = models.CharField(max_length=100)
#     correo_electronico = models.EmailField(unique=True)
#     profesion = models.CharField(max_length=100)
#     contrasenia = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     usuario_id = models.IntegerField()
#     REQUIRED_FIELDS = ['rol','nombre','apellidos' ,'profesion']
#     USERNAME_FIELD = 'correo_electronico'

class Doctor(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación uno a uno con Usuario
    apellidos = models.CharField(max_length=100)
    consultorio = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    telefono_celular = models.IntegerField()
    correo_electronico = models.CharField(max_length=100)

    #CONTRASENIA DE MARIA: MariaRe123


class Consultorio(models.Model):
    nombre_consultorio = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    capacidad_doctores = models.IntegerField()
    horarios = models.TimeField()
    numero_contacto = models.IntegerField()


class DoctorConsultorio(models.Model):
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    edad = models.IntegerField()
    ITS = models.BooleanField()
    problemas_cardiacos = models.BooleanField()
    diabetes = models.BooleanField()
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=100)
    


class HistorialClinico(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicamento = models.TextField()
    tratamiento = models.TextField()
    diagnostico = models.TextField()
    notas = models.TextField()


class Cita(models.Model):
    fecha_cita = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    detalle_cita = models.TextField()
    correo_electronico = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()


