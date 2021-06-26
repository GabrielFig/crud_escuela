from django import forms
from .models import Alumnos

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = "__all__"
        widgets = { 
            'nombre': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'apellido_paterno': forms.TextInput(attrs={ 'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={ 'class': 'form-control' }),
            'fecha_nac': forms.DateInput(attrs={ 'class': 'form-control datetimepicker-input',
                                                'type': 'date' }),
            'direccion': forms.TextInput(attrs={ 'class': 'form-control'}),
            'num_cel': forms.TextInput(attrs={ 'class': 'form-control' }),
            'semestre': forms.TextInput(attrs={ 'class': 'form-control' }),
            'correo': forms.EmailInput(attrs={ 'class': 'form-control' }),
        }