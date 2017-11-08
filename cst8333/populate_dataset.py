import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cst8333.settings")

import django
django.setup()

from first_app.models import Dataset
import csv

def populate_Dataset(file):
    try:   
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count > 0:
                dataset = Dataset()
                dataset.ref_date = row[0]
                dataset.geo = row[1],
                dataset.est = row[2],
                dataset.vector = row[3],
                dataset.coordinate = row[4],
                dataset.value = row[5]
                dataset.save()
            else:
                count+=1
            #New entry
        
    except Exception as e:
        print('Something went wrong "%s"'  % e)


''' 

Displays all of the lines inside a for loop without column titles, 

and when it displays each, count is increasing by 1.

'''


# Path of the provided dataset file.

filePath = "00010014-eng.csv"


# Opens dataset file and reading the records from loadDataset method.

if __name__ == '__main__':

    print("populating Database")
    with open(filePath, "r") as dataset:
        populate_Dataset(dataset)
    print("Complete!")




