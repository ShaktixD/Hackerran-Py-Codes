# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:32:20 2022

@author: shakti
"""

alphnum = False
alpha = False
num = False
lower = False
upper = False

x = input()
for i in x:
    if i.isalnum():
        alphnum = True
    if i.isalpha():
        alpha = True
        if i.islower():
            lower = True
        else:
            upper = True
    elif i.isdigit():
        num = True
    else:
        continue
print(alphnum,alpha,num,lower,upper,sep = '\n')