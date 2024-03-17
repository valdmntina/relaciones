from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.

def inicio(request):
  # reporter1= Reporter(first_name='Lucia', last_name='Pinto', email='luciapi@gmail.coom')
  # reporter1.save()

  # reporter2= Reporter(first_name='Paul', last_name='Jones', email='pauljo@gmail.com')
  # reporter2.save()

  # article1= Article(id=None, headline='esto es una prueba :p', pub_date= date(2003, 5, 20), reporter=reporter1)
  # article1.save()

  reporter = Reporter.objects.get(id=7)
  articles = reporter.article_set.all()
  return render(request, 'index.html', {
    'reporter': reporter,
    'articles': articles
  })


  # list = ""
  # for article in articles:
  #   list += article.headline
  
  # return HttpResponse(list)

def delete(request, id):
  eliminar = Reporter.objects.get(id=id)
  eliminar.delete()
  return HttpResponse('se elimino id')

def update(request, first_name, id):
  actualizar = Reporter.objects.get(id=id)
  actualizar.first_name = first_name
  actualizar.save()
  return HttpResponse('se actualizo el primer nombre del id 10')

def read(request, id):
  query = Reporter.objects.get(id=id)
  return render(request, 'index.html',{
    'query': query
  })
