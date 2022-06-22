from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

# las clases genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy

#------------CLASES GENERICS-----------------------------------------------
# --Otra forma usando clases Generics -------
class CarreraCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'Registro/carrera_form.html'
    success_url = reverse_lazy("add_pacientes")

class CarreraList(ListView):
    model = Paciente
    template_name = 'Registro/list_carreras.html'
    # paginate_by = 4

class CarreraUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'Registro/carrera_form.html'
    success_url = reverse_lazy('list_pacientes')

        

class CarreraDelete(DeleteView):
    model = Paciente
    template_name = 'Registro/carrera_delete.html'
    success_url = reverse_lazy('list_pacientes')
