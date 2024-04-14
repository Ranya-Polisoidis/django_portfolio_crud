from django.db import models

# Create your models here.

class Contact(models.Model):
    location = models.CharField(max_length=100)
    email = models.EmailField()
    call = models.CharField(max_length=20)
    iframe = models.TextField()
