from django.db import models
from django.urls import reverse
# Create your models here.

class Gunpla(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    description = models.TextField(max_length=250)


    def __str__(self):
        return f'{self.name}({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gunpla_id': self.id})
    
class Accessories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
