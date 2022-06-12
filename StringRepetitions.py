# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:00:26 2022

@author: shakti
"""

'''
def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)-len(sub_string)+1):
        check = string[i:i+len(sub_string)]
        if check == sub_string:
            counter +=1
    return counter
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
'''    
#====================== PRO METHOD ======================
x,xf = input(),input()
print([x[i:i+len(xf)] for i in range(len(x)+1-len(xf))].count(xf))