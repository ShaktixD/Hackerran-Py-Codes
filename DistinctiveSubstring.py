# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:31:44 2022

@author: shakti
"""
def filter(s):
    for i in range(len(s)):
        for j in s[i+1:]:
            if s[i] == j:
                s.pop(s[i+1:].index(j)+i+1)
    return s
                
def merge_the_tools(string, k):
    # your code goes here
    string = string.replace(" ","")
    x = [list(list(string[i:i+k])) for i in range(0,len(string),k)]
    final = [filter(i) for i in x]
    for i in range(len(string)//k):
        print(''.join(x[i]))

    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    