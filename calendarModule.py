# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:13:20 2022

@author: shakti
"""
import calendar
x = list(map(int,input().split()))
x.reverse()
dx = {0:'MON',1:"TUES",2:"WEDNES",3:'THURS',4:'FRI',5:'SATUR',6:'SUN'}
print(dx[calendar.weekday(x[0],x[2],x[1])]+'DAY')