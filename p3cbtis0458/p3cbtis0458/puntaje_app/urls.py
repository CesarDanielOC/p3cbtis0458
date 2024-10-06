from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index.html"),
    path("Médico/", views.Médico,name="Médico.html"),
    path("Paciente/", views.Paciente,name="Paciente.html"),
    path("Receta/", views.Receta,name="Receta.html"),
    path("Medicamento/", views.Medicamento,name="Medicamento.html"),
]