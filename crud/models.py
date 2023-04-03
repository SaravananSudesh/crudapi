from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    buy = models.FloatField()
    sell = models.FloatField()
    stock = models.BooleanField()
