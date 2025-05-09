#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:17:06 2024

@author: david
"""

class Augusto:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def no_hacer_platzi(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} y no hago platzi")
        
person1 = Augusto("Augusto", 11)
person1.no_hacer_platzi()