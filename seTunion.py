# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 2022

@author: shakti
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())
xe = set(map(int,input().split()))

y = int(input())
yf = set(map(int,input().split()))

print(len(xe.union(yf)))