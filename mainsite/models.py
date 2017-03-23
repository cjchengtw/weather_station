from django.db import models

# Create your models here.
class weather(models.Model):
    tpr = models.CharField(max_length=5)
    wet = models.CharField(max_length=5)
    ur = models.CharField(max_length=5)
    li = models.CharField(max_length=5)