from django.urls import path
from . import views

urlpatterns = [
  path('', views.inicio, name='inicio'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<str:name>/<int:id>', views.update, name='update'),
  path('read/<int:id>', views.read, name='read')
]