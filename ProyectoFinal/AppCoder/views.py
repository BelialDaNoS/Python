from django.shortcuts import render
from django.http import HttpResponse


def inicio_view (req):
    return HttpResponse("Bienvenidos")



def cursos_view(req):
    return render(req, "AppCoder/padre.html")

