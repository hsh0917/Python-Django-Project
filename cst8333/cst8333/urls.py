"""
File: urls.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file is mapping between URL patterns to index of views in first_app and list of URLs routes.

"""


from django.conf.urls import url, include
from django.contrib import admin
from first_app import views

# URLs routes maps to a views.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^first_app', include('first_app.urls')),
]
