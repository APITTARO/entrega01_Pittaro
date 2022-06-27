from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context, loader
from AppCoder.models import Familiar, TipoFamiliar, Hijos
from AppCoder.forms import FormularioBasico, FormularioParentezco, FormularioHijos

# Create your views here.

def Familiar1(self):
    familiar= Familiar(nombre="Alejandro", telefono=42598271, fechaNacimiento= date(2010,10,10))
    familiar.save()
    documento= f"Familiar--> Nombre: {familiar.nombre}  Telefono: {familiar.telefono} Fecha de Nacimiento: {familiar.fechaNacimiento}"
    return HttpResponse(documento)

def Familiar2(self):
    familiar= Familiar(nombre="Carmela", telefono=1587425896, fechaNacimiento= date(2000,12,12))
    familiar.save()
    documento= f"Familiar--> Nombre: {familiar.nombre}  Telefono: {familiar.telefono} Fecha de Nacimiento: {familiar.fechaNacimiento}"
    return HttpResponse(documento)

def Familiar3(self):
    familiar= Familiar(nombre="Ana", telefono=9441549, fechaNacimiento= date(2008,10,11))
    familiar.save()
    documento= f"Familiar--> Nombre: {familiar.nombre}  Telefono: {familiar.telefono} Fecha de Nacimiento: {familiar.fechaNacimiento}"
    return HttpResponse(documento)


def plantilla1(self):
    familiares = Familiar.objects.all()
    tipofamiliares = TipoFamiliar.objects.all()
    diccionario = {'familiares': familiares, 'tipo_familiares': TipoFamiliar, 'hijos': Hijos}
    plantilla = loader.get_template('template.html')

    documento= plantilla.render(diccionario)
    return  HttpResponse(documento)

def TipoFamiliar1(self):
    tipofamiliar= tipofamiliar(apellido="Perez", parentezco="Tío")
    tipofamiliar.save()
    documento= f"Tipo de Familiar--> Apellido: {tipofamiliar.apellido}  Parentezco: {tipofamiliar.parentezco}"
    return HttpResponse(documento)

def TipoFamiliar2(self):
    tipofamiliar= tipofamiliar(apellido="Castelucci", parentezco="Prima Lejana")
    tipofamiliar.save()
    documento= f"Tipo de Familiar--> Apellido: {tipofamiliar.apellido}  Parentezco: {tipofamiliar.parentezco}"
    return HttpResponse(documento)

def TipoFamiliar3(self):
    tipofamiliar= tipofamiliar(apellido="Perez", parentezco="Primo")
    tipofamiliar.save()
    documento= f"Tipo de Familiar--> Apellido: {tipofamiliar.apellido}  Parentezco: {tipofamiliar.parentezco}"
    return HttpResponse(documento)

def Hijos1 (self):
    hijos= Hijos(padre="Jorge Castelucci", madre ="", cant_hermanos= 2)
    hijos.save()
    documento= f"Hijos--> Padre: {hijos.padre}  Madre: {hijos.madre} Cantidad de Hermanos: {hijos.cant_hermanos}"
    return HttpResponse(documento)

def Hijos2 (self):
    hijos= Hijos(padre="Andres Andrada", madre ="Carla Ibañez", cant_hermanos= 0)
    hijos.save()
    documento= f"Hijos--> Padre: {hijos.padre}  Madre: {hijos.madre} Cantidad de Hermanos: {hijos.cant_hermanos}"
    return HttpResponse(documento)

def Hijos3 (self):
    hijos= Hijos(padre="", madre ="Sandra Riguera", cant_hermanos= 4)
    hijos.save()
    documento= f"Hijos--> Padre: {hijos.padre}  Madre: {hijos.madre} Cantidad de Hermanos: {hijos.cant_hermanos}"
    return HttpResponse(documento)

def FormularioBasico1(request):

    if request.method=='POST':
        primerformulario = FormularioBasico (request.POST)

        print(primerformulario)

        if primerformulario.is_valid:
            info= primerformulario.cleaned_data
            familiar= Familiar (nombre= info['nombre'], telefono= info['telefono'], fechaNacimiento= info['fechaNacimiento'])
            familiar.save()
            return render(request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\template.html")
        else:
            primerformulario = FormularioBasico()

            return render (request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\formularioBasico.html", {'primerformulario': primerformulario})

def FormularioParentezco1(request):
    if request.method=='POST':
        segundoformulario = FormularioParentezco (request.POST)

        print(segundoformulario)

        if segundoformulario.is_valid:
            info= segundoformulario.cleaned_data
            parentezco= TipoFamiliar (apellido= info['apellido'], parentezco= info['parentezco'])
            parentezco.save()
            return render(request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\template.html")
        else:
            segundoformulario = FormularioParentezco()
            return render (request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\formularioParentezco.html",{'segundoformulario': segundoformulario})

def FormularioHijos1(request):
    if request.method=='POST':
        tercerformulario = FormularioHijos (request.POST)

        print(tercerformulario)

        if tercerformulario.is_valid:
            info= tercerformulario.cleaned_data
            familiacercana= Hijos (padre= info['apellido'], madre= info['parentezco'], cant_hermanos= info['cant_hermanos'])
            familiacercana.save()
            return render(request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\template.html")
        else:
            tercerformulario = FormularioHijos()
    return render (request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\formularioHijos.html",{'tercerformulario': tercerformulario})


def buscar (request):
    if request.GET["nombre"]:
        nombre= request.GET['nombre']
        print(nombre)
        familiares = Familiar.objects.filter(nombre__icontains=nombre)
        print(familiares)
        return render(request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\resultadobusqueda.html", 
        {"familiares": familiares, "nombre": nombre})

    else: 
        respuesta= "No enviaste datos"
        return render (request, "C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\AppCoder\\plantillas\\resultadobusqueda.html", {"respuesta": respuesta})