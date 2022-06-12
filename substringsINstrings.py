# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:51:09 2022

@author: shakti
"""

def count_substring(string, sub_string):
    slen = len(string)
    sslen = len(sub_string)
    Lstring = list(string)
    Lsubstring = list(sub_string)
    
    for i in range(sslen):
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)