from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

# Create your views here.

def inicio(request):
  # publica1= Publication(title='Noticias de ciencia')
  # publica1.save()

  # article1= Article(headline='en Japon se cayó un gato en desechos toxicos, se escapo y si lo encuentran lo hacen caldo.')
  # article1.save()

  # publica2= Publication(title= 'Noticias de farandula')
  # publica2.save()

  # article2= Article(headline= "No se nada de farandula xdd")
  # article2.save()

  # publica3= Publication(title= 'Noticias nacionales')
  # publica3.save()

  # article3= Article(headline= 'En la marcha de uribistas habian puros viejitos que olian a formol')
  # article3.save()

  # article1.publication.add(publica1)
  # article2.publication.add(publica2)
  # article3.publication.add(publica3)

#CON ESTO ELIMINE PUBLICATIONS REPETIDAS
  eliminar = Publication.objects.get(id=5)
  eliminar.delete()
  eliminar = Publication.objects.get(id=6)
  eliminar.delete()
  eliminar = Publication.objects.get(id=7)
  eliminar.delete()

#CON ESTO ELIMINE ARTICLES REPETIDAS
  eliminar = Article.objects.get(id=4)
  eliminar.delete()
  eliminar = Article.objects.get(id=5)
  eliminar.delete()
  eliminar = Article.objects.get(id=6)
  eliminar.delete()

 
  return HttpResponse('sirvio esta porqueria 10.0')

def update(request, title, id):
  actualizar = Publication.objects.get(id=id)
  actualizar.title = title
  actualizar.save()
  return HttpResponse('se actualizo el titulo del id 1')

def read(request, id):
  query = Publication.objects.get(id=id)
  return render(request, 'muchosamuchos.html',{
    'query': query
  })