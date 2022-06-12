from itertools import groupby
new = input()
new = groupby(new)
new = [(k,v) for k,v in list(new)]