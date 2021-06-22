from core.forms import SolicitudForm
from django.shortcuts import redirect, render
from .models import Solicitud
# Create your views here.

def home(request):
    solicitudes = Solicitud.objects.all()
    datos = {
        'solicitudes': solicitudes
    }
    return render(request, 'home.html', datos)

def galeria(request):
       
    return render(request, 'galeria.html')

def quienessomos(request):
        
    return render(request, 'quienessomos.html')

def contacto(request):
        
    return render(request, 'contacto.html')

def contratacion(request):
    if request.method=='POST': 
        solicitud_form = SolicitudForm(request.POST)
        if solicitud_form.is_valid():
            solicitud_form.save()
            return redirect('home')
    else:
        solicitud_form= SolicitudForm()
    return render(request, 'contratacion.html', {'solicitud_form': solicitud_form})


def vercontrataciones(request):
    solicitudes = Solicitud.objects.all()
    datos = {
        'solicitudes': solicitudes
    }
    return render(request, 'vercontrataciones.html', datos)

def form_mod_solicitud(request,id):
    solicitud = Solicitud.objects.get(rut=id)

    datos ={
        'form': SolicitudForm(instance=solicitud)
    }
    if request.method == 'POST': 
        formulario = SolicitudForm(data=request.POST, instance = solicitud)
        if formulario.is_valid: 
            solicitud.delete()
            formulario.save()    
            return redirect('vercontrataciones')
    return render(request, 'form_mod_solicitud.html', datos)

def form_del_solicitud(request,id):
    solicitud = Solicitud.objects.get(rut=id)
    solicitud.delete()
    return redirect('vercontrataciones')



