'''
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

returns a generator object, use a list to demonstrate of cartesian products of 2 iterables
itertools.product(iterable,repeat = 2)

'''
from itertools import product
print(*list(product(list(map(int,input().split())),list(map(int,input().split())))))