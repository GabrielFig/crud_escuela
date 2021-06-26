from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnos
from .forms import AlumnoForm
from django.views.generic import ListView, DetailView


def home_alumno(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'crudapp/index.html', { 'alumnos': alumnos })

class AlumnoDetailView(DetailView):
    model = Alumnos
    template_name = 'crudapp/alumno-detail.html'

def create(request):
    if request.method == "POST":  
        form = AlumnoForm(request.POST)  
        if form.is_valid():  
            obj = Alumnos()
            obj.nombre = form.cleaned_data['nombre']
            obj.apellido_paterno = form.cleaned_data['apellido_paterno']
            obj.apellido_materno = form.cleaned_data['apellido_materno']
            obj.direccion = form.cleaned_data['direccion']
            obj.fecha_nac = form.cleaned_data['fecha_nac']
            obj.semestre = form.cleaned_data['semestre']
            obj.num_cel = form.cleaned_data['num_cel']
            obj.correo = form.cleaned_data['correo']
            obj.horario_alumno = form.cleaned_data['horario_alumno']
            obj.save()
            print("se guardo al alumno")
            
            return redirect('index')    
        else:
            print(form.errors.as_data())
    else:  
        form = AlumnoForm()  
    return render(request,'crudapp/create.html',{'form':form})  

def edit(request, pk, template_name='crudapp/edit.html'):
    alumno = get_object_or_404(Alumnos, pk=pk)
    form = AlumnoForm(request.POST or None, instance=alumno)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    alumno = get_object_or_404(Alumnos, pk=pk)
    if request.method=='POST':
        alumno.delete()
        return redirect('index')
    return render(request, template_name, {'object':alumno})
