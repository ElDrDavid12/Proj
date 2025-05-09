#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:23:40 2025

@author: david
"""

class LivingBeing:
    def __init__(self, name):
        self.name = name
        
class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age 
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

student = Student("Victor", 13, "3279866@tpsdonline.org")
student.introduce()