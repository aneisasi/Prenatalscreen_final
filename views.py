from django.shortcuts import render

def home(request):
    context = {
        'titulo': '¡Bienvenido a tu sitio web!',
        'mensaje': 'Esta es tu primera página creada con Django y Docker',
    }
    return render(request, 'home.html', context)

from django.shortcuts import render

def home(request):
    context = {
        'titulo': '¡Bienvenido a tu sitio web!',
        'mensaje': 'Esta es tu primera página creada con Django y Docker',
    }
    return render(request, 'home.html', context)

def plantilla1(request):
    return render(request, 'plantilla1.html', {'titulo': 'Plantilla 1', 'descripcion': 'Primera página de ejemplo', 'contenido': 'Contenido de la plantilla 1'})

def plantilla2(request):
    return render(request, 'plantilla2.html', {'titulo': 'Plantilla 2', 'descripcion': 'Segunda página de ejemplo', 'contenido': 'Contenido de la plantilla 2'})

def plantilla3(request):
    return render(request, 'plantilla3.html', {'titulo': 'Plantilla 3', 'descripcion': 'Tercera página de ejemplo', 'contenido': 'Contenido de la plantilla 3'})

def plantilla4(request):
    return render(request, 'plantilla4.html', {'titulo': 'Plantilla 4', 'descripcion': 'Cuarta página de ejemplo', 'contenido': 'Contenido de la plantilla 4'})