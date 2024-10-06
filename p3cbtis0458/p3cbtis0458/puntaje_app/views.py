from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def Médico(request):
    return render(request, "Médico.html")

def Paciente(request):
    return render(request, "Paciente.html")

def Receta(request):
    return render(request, "Receta.html")

def Medicamento(request):
    return render(request, "Medicamento.html")