# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:10:24 2022

@author: shakti
"""

#country stamps

collection = set()
x = int(input())
for i in range(x):
    val = input()
    val = val.lower()
    collection.add(val)
    
print(len(collection))