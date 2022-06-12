# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:33:19 2022

@author: shakt
"""


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    m3 = set([i for i in range(n) if i % 3 ==0])
    m5 = set([i for i in range(n) if i % 5 ==0])
    m15 = m3.intersection(m5)
    
    for i in range(n):
        if i in m15:
            print("FizzBuzz")
        elif i in m3:
            print("Fizz")
        elif i in m5:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
