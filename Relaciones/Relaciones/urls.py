
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('uno/', include('unoauno.urls'), name='unoauno.urls'),
    path('unoamuchos/', include('unoamuchos.urls'), name='unoamuchos.urls'),
    path('muchosamuchos/', include('muchosamuchos.urls'), name='unoamuchos.urls'),
]
