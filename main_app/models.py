from django.db import models

# Create your models here.

class Gunpla(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    description = models.TextField(max_length=250)


def __str__(self):
    return f'{self.name}({self.id})'
