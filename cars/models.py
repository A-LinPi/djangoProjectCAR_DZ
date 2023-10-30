from django.db import models


# Create your models here.
class Cars(models.Model):
    mark = models.CharField('марка авто', max_length=20)
    manufacturer = models.CharField('производитель', max_length=20)
    year = models.IntegerField('год')
    gos_number = models.CharField('гос номер', max_length=11)
    objects = models.Manager()
