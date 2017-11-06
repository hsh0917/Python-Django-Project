from django.db import models

# Create your models here.

class dataset(models.Model):
    ref_date = models.DecimalField(max_digits=4, decimal_places=0)
    geo = models.CharField(max_length=40)
    est = models.CharField(max_length=150)
    vector = models.CharField(max_length=6)
    coordinate = models.CharField(max_length=4)
    value = models.DecimalField(max_digits=10, decimal_places=0)
