from django.contrib import admin
from django.urls import path
from AppCoder.views import Familiar1, Familiar2, Familiar3, TipoFamiliar1, TipoFamiliar2, TipoFamiliar3, Hijos1, Hijos2, Hijos3, FormularioBasico1, FormularioParentezco1, FormularioHijos1, buscar 



urlpatterns = [
    path('admin/', admin.site.urls),
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
]