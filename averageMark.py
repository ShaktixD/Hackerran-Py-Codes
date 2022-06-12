# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:31:07 2022

@author: shakti
"""

def splitter(value):
    global records
    temp = value.split()
    name = temp.pop(0)
    for i in range(len(temp)):
        temp[i] = float(temp[i])
    records[name] = temp
    
        

x = int(input())
records = {}
for i in range(x):
    val = input()
    splitter(val)  
x = input()
average = sum(records[x])
average = round(average/3,2)
print(format(average,'.2f'))