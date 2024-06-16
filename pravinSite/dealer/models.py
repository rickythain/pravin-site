from django.db import models
from login import models as login_models

class Dealer(models.Model):
  id = models.IntegerField(primary_key=True)
  user_id = models.ForeignKey(login_models.User, on_delete=models.CASCADE)
  company_name = models.CharField(max_length=150)
  contact_info = models.CharField(max_length=150)