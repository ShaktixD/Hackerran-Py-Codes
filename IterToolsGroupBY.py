# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:31:22 2022

@author: shakti
"""
#shows the count and the key respectively !

from itertools import groupby
x = groupby(input())
v = [(len(list(y)),k) for k,y in x]
for i in v:
    print(i,end = ' ')