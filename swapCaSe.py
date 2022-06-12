# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:31:27 2022

@author: shakti
"""

sent  = input()
outp = '' 
if len(sent) <= 1000:
    for i in range(len(sent)):
        if sent[i].isupper() == True:
            outp += sent[i].lower()
        elif sent[i].islower() == True:
            outp += sent[i].upper()
        else:
            outp += sent[i]

print(outp)