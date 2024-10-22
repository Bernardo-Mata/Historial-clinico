from django import forms
from .models import HistorialClinico
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import HistorialClinico, Paciente
from django.contrib.auth.models import User

class HistorialClinicoForm(forms.ModelForm):
    class Meta:
        model = HistorialClinico
        fields = "__all__"


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        