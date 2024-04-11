from django.db import models

# Create your models here.

class Skills(models.Model):
    langages = models.CharField(max_length=100)
    percentage= models.IntegerField()

