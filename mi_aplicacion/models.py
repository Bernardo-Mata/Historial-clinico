from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    usuario_id = models.IntegerField()


class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    consultorio = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    telefono_celular = models.IntegerField()
    correo_electronico = models.CharField(max_length=100)


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
    correo_electronico = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()


class HistorialClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
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


