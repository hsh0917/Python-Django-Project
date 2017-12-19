"""
File: tests.py
Author: Seokhwan Lee
Date: Nov 29, 2017
Description: This file is a conventional place for an application’s tests. 
             The testing system will automatically find tests in any file whose name begins with test.
"""
from django.test import TestCase
from .models import Dataset
# Unit test for database I stored
class DatasetTests(TestCase):
    def test_geo(self):
        dataset = Dataset(ref_date='1909',
                          geo="Canada",
                          est="Seeded area, potatoes (acres)",
                          vector="v47140",
                          coordinate="1.1",
                          value="504382")

        self.assertEquals(
            str(dataset),
            dataset.geo
        )

