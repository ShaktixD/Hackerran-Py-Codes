
'''
itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
'''

from itertools import permutations

x = input().split()
value = sorted(list(permutations(x[0],int(x[1]))))
print(*[''.join(i) for i in value],sep = '\n')