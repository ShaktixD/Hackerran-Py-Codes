# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:26:46 2022

@author: shakti
"""
#set operation shit

m_size = int(input())
m = input().split()
m = set(map(int,m))

n_size = int(input())
n = input().split()
n = set(map(int,n))

temp = list(m-n)+list(n-m)
temp.sort()
for i in temp:
    print(i)