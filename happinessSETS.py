# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:26:46 2022

@author: shakti
"""
#happiness if found in a but sad if found in b, (a & b are disjoint sets)
size = input().split()
n_size,m_size = list(map(int,size))
check = []

x = input().split()
check = list(map(int,x))

a_in = input().split()
a = set(map(int,a_in))

b_in = input().split()
b = set(map(int, b_in))

happiness = 0

for i in range(n_size):
    if check[i] in a:
        happiness +=1
    else:
        happiness -= 1
        
print(happiness)