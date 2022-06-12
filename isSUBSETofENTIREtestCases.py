# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:49:33 2022

@author: shakti
"""

baap = set(map(int,input().split()))
flag = 1
for i in range(int(input())):
    gay = set(map(int,input().split()))
    if not gay.issubset(baap):
        flag =0
print(bool(flag))