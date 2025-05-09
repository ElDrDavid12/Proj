#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:51:34 2024

@author: david
"""

name = input("Hello! What's your name? ").title()
print(f"\n Hi, {name}! How are you feeling today? \n 1. Happy 🙂\n 2. Stressed 😟 \n 3. Tired 😫")
mood = int(input("Choose 1, 2, or 3: "))
mood = str(mood)
if mood == "1":
    print(f"That's great, {name}! Keep streading your joy")
elif mood == "2":
    print(f"Take a deep breath, {name}. You're doing amazing!")
else:
    print(f"Rest up, {name}. Tomorrow is a fresh start!")