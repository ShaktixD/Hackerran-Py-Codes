# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 2022

@author: shakti
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

name = input().split()

for i in range(len(name)):
    name[i] = name[i].capitalize()
    
print(' '.join(name))