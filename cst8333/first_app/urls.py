"""
File: urls.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file is mapping between URL patterns to index of views in first_app.

"""
from django.conf.urls import url
from first_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
