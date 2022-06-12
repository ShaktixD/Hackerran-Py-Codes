'''
.symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
leng = int(input())
eng = set(map(int,input().split()))
lfre = int(input())
fre = set(map(int,input().split()))

print(len(eng.symmetric_difference(fre)))