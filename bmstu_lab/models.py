

# Create your models here.
from django.db import models

# Create your models here.


class Priziv(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    categoriya = models.CharField(max_length=30)
    vozrast = models.CharField(max_length=30)
    otsrochka = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'prizivniki'