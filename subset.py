# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:51:11 2022

@author: shakti
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    x = input() #set_sizes
    setX = set(map(int,input().split()))
    t = input() #set_sizes
    setY = set(map(int,input().split()))
    print(True if len(list(setX-setY)) == 0 else False)