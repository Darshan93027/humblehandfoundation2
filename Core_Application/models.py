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
    


# from django.db import models

# # Create your models here.
# from django.db import models


# from django.db import models

# class User(models.Model):
#     google_id = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     picture = models.URLField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.email
    

class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # Store plain text only for demo (use hashing in real apps)

    def __str__(self):
        return self.username