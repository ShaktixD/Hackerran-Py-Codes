# -*- coding: utf-8 -*-
"""
Created on Mon May  2 01:12:06 2022

@author: shakti
"""
import numpy as np
np.set_printoptions(legacy='1.13')
x = np.array(input().split(),float)
print(np.floor(x),np.ceil(x),np.rint(x),sep = '\n')
#different operations on numpy array
'''
import numpy as np
x,y = list(map(int,input().split()))
a1 = np.array([input().split() for i in range(x)],int)
a2 = np.array([input().split() for i in range(x)],int)
print(a1+a2,
      a1-a2,
      a1*a2,
      a1//a2,
      a1%a2,
      a1**a2,sep='\n')
'''
#You are given the coefficients of a polynomial P Your task is to find the value of P at point x
'''
import numpy as np
x = list(map(float,input().split()))
print(np.polyval(x,int(input())))
'''
#inner and outer product
'''
import numpy as np
arr1 = np.array(input().split(),int)
arr2 = np.array(input().split(),int)
print(np.inner(arr1,arr2),np.outer(arr1,arr2),sep = '\n')
'''

#determinant of 2 arrays
'''
import numpy as np
arra = np.array([input().split() for i in range(int(input()))],float)
x = print(round(np.linalg.det(arra),2))

'''
#matrix product of 2 arrays
'''
import numpy as np
x = int(input())
val1 = np.array([input().split() for i in range(x)],int)
val2 = np.array([input().split() for i in range(x)],int)
print(np.dot(val1, val2))

#print(np.cross(val1,val2)), not used here
'''