from django.db import models

# Create your models here.
class volunteer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    msg= models.TextField(max_length=400)
    date = models.CharField(max_length=10)  # 10 characters for the dd/mm/yyyy format
      # Time field in 12-hour format (hh:mm AM/PM)
    time = models.CharField(max_length=8)  # 8 characters for the hh:mm AM/PM format

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"