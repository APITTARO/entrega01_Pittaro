"""mvt_pittaro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mvt_pittaro.views import saludo,dia_de_hoy, Nombre, fecha_cumple, template
from AppCoder.views import template, Familiar1, Familiar2, Familiar3, TipoFamiliar1, TipoFamiliar2, TipoFamiliar3, Hijos1, Hijos2, Hijos3, FormularioBasico1, FormularioParentezco1, FormularioHijos1, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path ('dia_de_hoy/',dia_de_hoy),
    path('Nombre/<nombre>', Nombre),
    path('fecha_cumple/<fecha>', fecha_cumple),
    path('Familiar/', Familiar1),
    path('Familiar/', Familiar2),
    path('Familiar/', Familiar3),
    path('TipoFamiliar/', TipoFamiliar1),
    path('TipoFamiliar/', TipoFamiliar2),
    path('TipoFamiliar/', TipoFamiliar3),
    path('Hijos/', Hijos1),
    path('Hijos/', Hijos2),
    path('Hijos/', Hijos3),
    path('FormularioBasico/', FormularioBasico1),
    path('FormularioParentezco/', FormularioParentezco1),
    path('FormularioHijos/', FormularioHijos1),
    path('buscar/', buscar),
    path('template/', template),
]

