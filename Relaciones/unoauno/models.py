from django.db import models

# Create your models here.

class Place(models.Model):
  name=models.CharField(max_length=50)
  address=models.CharField(max_length=50)

class Restaurant(models.Model):
  place=models.OneToOneField(Place,
                               on_delete=models.CASCADE, primary_key=True)
  employess=models.IntegerField(default=1)