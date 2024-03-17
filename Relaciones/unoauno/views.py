from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.

def inicio(request):
  # place1 = Place(name='Centro', address='Cra 12 #13-16')
  # place1.save()

  # restaurante1= Restaurant(place=place1, employess=3)
  # restaurante1.save()

  restaurante = Restaurant.objects.get(place_id=1)
  print(restaurante.place.address)


  return HttpResponse('Datos guardados correctamente')

def delete(request, id):
  eliminar = Place.objects.get(id=id)
  eliminar.delete()
  return HttpResponse('se elimino id ')

def update(request, name, id):
  actualizar = Place.objects.get(id=id)
  actualizar.name = name
  actualizar.save()
  return HttpResponse('se actualizo el nombre del unico id')

def read(request, id):
  query = Restaurant.objects.get(place_id=id)
  return render(request, 'unoauno.html',{
    'query': query
  })
