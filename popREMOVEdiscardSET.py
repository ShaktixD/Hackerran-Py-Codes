# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:26:46 2022

@author: shakti
"""

bagElem = int(input())                        #for num of set elements
x = input().split()                           #for set elements
limit = int(input())                          #for num of commands
for i in range(len(x)):
    x[i] = int(x[i])
bag = set(x)
for i in range(limit):
    statement = input().split()
    if statement[0] == 'remove':
        statement[1] = int(statement[1])
        if statement[1] in bag:
            bag.remove(statement[1])
    elif statement[0] == 'pop':
        bag.pop()
    else:
        statement[1] = int(statement[1])
        bag.discard(statement[1])
        
print(bag)