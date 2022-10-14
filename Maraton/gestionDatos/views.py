from django.shortcuts import render

# Create your views here.
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render

def malladoVial(request):
    lista=["Sebastián","Fercho","Lisseth"]
    variable=98
    return render(request,"index.html",{"Variable":variable,"Nombres":lista})