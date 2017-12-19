"""
File: models.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file is implemented as subclasses of django.db.models.Model and include fields.

"""

from django.db import models

# Create your models here.

# To save provided dataset from professor into database, This defines database table.
# ref_date, geo, est, vector, coordinate, value will be column of database table.
class Dataset(models.Model):
    # ref_date
    ref_date = models.CharField(max_length=4)
    # geo
    geo = models.CharField(max_length=40)
    # est
    est = models.CharField(max_length=150)
    # vector
    vector = models.CharField(max_length=6)
    # coordinate
    coordinate = models.CharField(max_length=4)
    # value
    value = models.CharField(max_length=10)
    
    def __str__(self):
        return self.geo
        
