from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    
    # localhost:8000/add_carrera
    path('add_pacientes', views.CarreraCreate.as_view(), name="add_pacientes"),

    path('list_pacientes', views.CarreraList.as_view(), name="list_pacientes"),

    # Crear la ruta para eliminar y modificar por GENERICS    
    path('del_paciente/<pk>', views.CarreraDelete.as_view(), name="del_pacientes"),
    
    path('update_paciente/<pk>', views.CarreraUpdate.as_view(), name="update_pacientes"),
    
    
]