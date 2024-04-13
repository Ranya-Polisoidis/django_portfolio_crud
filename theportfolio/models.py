from django.db import models

# Create your models here.

class Theportfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    filter = models.CharField(max_length=50)
