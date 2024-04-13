from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    class_css = models.CharField(max_length=100)
