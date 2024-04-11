from django.db import models

# Create your models here.

class Facts(models.Model):
    client_count = models.IntegerField()
    projects_count = models.IntegerField()
    support_hours = models.IntegerField()
    workers_count = models.IntegerField()


