"""
File: admin.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file is Django’s command-line utility for administrative tasks.

"""
from django.contrib import admin
from first_app.models import Dataset
# Register your models here.

# Adding a database in admin site
admin.site.register(Dataset) 
