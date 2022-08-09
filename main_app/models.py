from django.db import models

# Create your models here.

class Yarn(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    color = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.brand} {self.name} ({self.id})'