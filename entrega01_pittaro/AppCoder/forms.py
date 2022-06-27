from django import forms

class FormularioBasico (forms.Form):
    nombre=forms.CharField(max_length=100)
    telefono= forms.IntegerField()
    fechaNacimiento=forms.DateTimeField()

class FormularioParentezco (forms.Form):
    apellido= forms.CharField(max_length=200)
    parentezco= forms.CharField(max_length=100)

class FormularioHijos (forms.Form):
    padre= forms.CharField(max_length=200)
    madre= forms.CharField(max_length=200)
    cant_hermanos= forms.IntegerField()