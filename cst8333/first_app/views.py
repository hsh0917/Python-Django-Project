"""
File: views.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file will request information from the model I created before and pass it to a template.

"""
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Dataset # To use dataset which is stored in database, import the Dataset table from models.

# Create your views here.


def index(request):
    dataset_list = Dataset.objects.order_by('ref_date')  # dataset_list is a key and going to be the variable that we pass into that template tag in HTML.
    date_dict = {'dataset': dataset_list}
    return render(request, 'first_app/index.html', context=date_dict) # First parameter: template we wish to use.  Second parameter: Actual file. Third parameter: context. this passin to our index.html


