# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:31:08 2022

@author: shakti
"""


x = int(input())
records = []
marksL = []
for i in range(x):
    name = input()
    marks = float(input())
    marksL.append(marks)
    records.append([name,marks])
#==============================
#here its second lowest
highest = min(marksL)
marksL= [i for i in marksL if i != highest]
highest = min(marksL)
names = []
for i in range(len(records)):
    if records[i][1] == highest:
        names.append(records[i][0])

names.sort()
for x in names:
    print(x)