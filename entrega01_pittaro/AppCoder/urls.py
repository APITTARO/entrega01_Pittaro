from django.contrib import admin
from django.urls import path
from AppCoder.views import plantilla1, template, Familiar1, Familiar2, Familiar3, TipoFamiliar1, TipoFamiliar2, TipoFamiliar3, Hijos1, Hijos2, Hijos3, FormularioBasico1, FormularioParentezco1, FormularioHijos1, buscar



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Familiar1/', Familiar1),
    path('Familiar2/', Familiar2),
    path('Familiar3/', Familiar3),
    path('TipoFamiliar1/', TipoFamiliar1),
    path('TipoFamiliar2/', TipoFamiliar2),
    path('TipoFamiliar3/', TipoFamiliar3),
    path('Hijos1/', Hijos1),
    path('Hijos2/', Hijos2),
    path('Hijos3/', Hijos3),
    path('FormularioBasico1/', FormularioBasico1),
    path('FormularioParentezco1/', FormularioParentezco1),
    path('FormularioHijos1/', FormularioHijos1),
    path('buscar/', buscar),
    path('template/', template),
    path('plantilla1/', plantilla1),
]