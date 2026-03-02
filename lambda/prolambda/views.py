from django.shortcuts import render
from .models import prolambda

def lista_productos(request):

    productos = list(prolambda.objects.all())

    productos_ordenados = sorted(productos, key=lambda p: p.precio)

    return render(request, "productos.html", {
        "productos": productos_ordenados
    })