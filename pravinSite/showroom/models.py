from django.db import models
from dealer import models as dealer_models

class Car(models.Model):
  id = models.IntegerField(primary_key=True)
  dealer_id = models.ForeignKey(dealer_models.Dealer, on_delete=models.CASCADE)
  model = models.CharField(max_length=200)
  make = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=20)
  image = models.CharField(max_length=100)
  description = models.TextField()