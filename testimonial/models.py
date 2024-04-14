from django.db import models

# Create your models here.

class Testimonial(models.Model):
    comment = models.TextField()
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
