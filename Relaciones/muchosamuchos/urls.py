from django.urls import path
from . import views


urlpatterns = [
   path('', views.inicio, name='inicio'),
   path('update/<str:title>/<int:id>', views.update, name='update'),
   path('read/<int:id>', views.read, name='read')
]