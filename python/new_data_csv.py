#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:29:44 2025

@author: david
"""

import csv

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargerMaster",
    "category": "Accesories",
    "entry_date": "2025-22-01"
}

with open('/home/david/Downloads/csv/products.csv', mode='a') as file:
    file.write("\n")
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)