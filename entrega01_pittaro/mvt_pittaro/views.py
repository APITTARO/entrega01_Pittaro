from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context
from django.template import loader


def saludo(request):
    return HttpResponse("Hola Django-Coder")

def dia_de_hoy(request):
    
    dia = datetime.datetime.now()

    documento_de_Texto = f"</br></br>Hoy es: {dia}"
    return HttpResponse(documento_de_Texto)

def Nombre (self, nombre):
    documento_de_Texto = f"El usuario se llama: </br> {nombre}"

    return HttpResponse(documento_de_Texto)

def fecha_cumple (request,fecha):
    fecha_actual= date.today()
    anio = fecha_actual.year
    fecha = int(fecha)

    resultado = anio - fecha

    cumpleanio = f"El año de nacimiento es: {resultado}"
    return HttpResponse(cumpleanio)

def template(self):
    html = open("C:\\Users\\agus-\\Desktop\\python\\django\\nuevo_proyecto\\mvt_pittaro\\mvt_pittaro\\plantillas\\template.html")
    
    plantilla = Template(html.read())
    
    html.close()
    
    contexto = Context()
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)