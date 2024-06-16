from django.db import models

class User(models.Model):
  id = models.IntegerField(primary_key=True)
  username = models.CharField(max_length=150)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  email = models.CharField(max_length=254)
  password = models.CharField(max_length=128)