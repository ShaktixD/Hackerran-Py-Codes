# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 2022

@author: shakti
"""

# ++++++++++++++++++++ NAMED TUPLE FROM COLLECTIONS LIBRARY +++++++++++++++

from collections import namedtuple
n, nt = int(input()), namedtuple('Student', input())
records = [nt(*input().split()) for i in range(n)]
print(format(sum([float(i.MARKS) for i in records])/n,"0.2f"))