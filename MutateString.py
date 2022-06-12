# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:40:53 2022

@author: shakti
"""

def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    
    #===========================================
    #another way is to use string = list(string)
    #string[position] = character
    #"".join(string)
    #===========================================
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)