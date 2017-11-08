from django.db import models

# Create your models here.

class Dataset(models.Model):
    ref_date = models.CharField(max_length=4)
    geo = models.CharField(max_length=40)
    est = models.CharField(max_length=150)
    vector = models.CharField(max_length=6)
    coordinate = models.CharField(max_length=4)
    value = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Dataset
