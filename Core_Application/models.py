from django.db import models

# Create your models here.
class volunteer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    msg= models.TextField(max_length=400)
    