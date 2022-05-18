from django.db import models

# Create your models here.

class Familiar(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth_date = models.DateField()