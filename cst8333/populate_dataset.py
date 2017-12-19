"""
File: populate_dataset.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description:  This file reads data from given csv file, and populate it into database.

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cst8333.settings")

import django
django.setup()

from first_app.models import Dataset
import csv


#  Read data from csv and populate it into models.
def populate_Dataset(file, delimiter =", "):
    try:   
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count > 0:
                dataset = Dataset()
                dataset.ref_date = row[0]
                dataset.geo = row[1]
                dataset.est = row[2]
                dataset.vector = row[3]
                dataset.coordinate = row[4]
                dataset.value = row[5]
                dataset.save()
            else:
                count+=1
            
        
    except Exception as e:
        print('Something went wrong "%s"'  % e)




# Path of the provided dataset file.
filePath = "00010014-eng.csv"


# Opens dataset file and reading the records from loadDataset method.
if __name__ == '__main__':

    print("populating Database")
    with open(filePath, "r") as dataset:
        populate_Dataset(dataset)
    print("Complete!")




