"""
File: apps.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file is created to help the user include any application configuration for the app. 
            Using this, you can configure some of the attributes of the application.

"""
from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    name = 'first_app'
