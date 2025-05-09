#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:48:58 2024

@author: david
"""
contacts = {"Victor D.":{"Apellido":"Arrieta","ALtura":1.64,"Edad":13},
            "Augusto":{"Apellido":"Arrieta","ALtura":"N/A","Edad":11},
            "Victor J.":{"Apellido":"Arrieta","ALtura":1.72,"Edad":45}}
user = input("Information of Victor D., Augusto, and Victor J.: ")
print(contacts[user])