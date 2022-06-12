# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 2022

@author: shakti
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    try:
        number1,number2 = map(int,input().split())
        print(number1//number2)
        
        
    except Exception as e:
        print("Error Code:",e)
'''       
   except ValueError as v:
       print("Error Code",v)
   except ZeroDivisionError as z:
       print("Error Code",z)
       
       
    =============   NOT WORKING =========
    
'''
