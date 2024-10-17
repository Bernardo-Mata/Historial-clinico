from django import forms
from .models import HistorialClinico


from django import forms
from .models import HistorialClinico, Paciente

class HistorialClinicoForm(forms.ModelForm):
    class Meta:
        model = HistorialClinico
        fields = "__all__"


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"