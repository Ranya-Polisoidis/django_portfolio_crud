from django.db import models

# Create your models here.

class About(models.Model):

    # Profile
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)

    # Informations de base
    birthday = models.DateField()
    website = models.URLField(max_length=200)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    # Informations supplémentaires
    age = models.PositiveSmallIntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)

    # Informations complémentaires
    description = models.TextField()
    profession = models.CharField(max_length=100)
    about_you = models.TextField() 
    more_info = models.TextField() 
