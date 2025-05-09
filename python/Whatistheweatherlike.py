#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:34:30 2024

@author: david
"""

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}
print("What's the weather like today?")
print("1. Sunny\n 2. Rainy\n 3. Cloudy\n 4. Snowy")
choice = input("choose 1, 2, 3 or 4: ")
if choice == "1":
    print(weather_activities["1"])
elif choice == "2":
    print(weather_activities["2"])
elif choice =="3":
    print(weather_activities["3"])
else:
    print(weather_activities["4"])